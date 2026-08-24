from decimal import Decimal
from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from .models import CashFlowTwin, CashFlowEntry, ForecastPoint
from .serializers import CashFlowTwinSerializer, CashFlowEntrySerializer, ForecastPointSerializer
from .builder import build_cashflow_twin
from .tasks import rebuild_twin


def serialize_invoice_status(invoice):
    from django.utils import timezone
    today = timezone.localdate()
    outstanding = float(invoice.outstanding_amount)
    if outstanding <= 0:
        status = "paid"
        days_overdue = 0
    elif invoice.due_date < today:
        status = "overdue"
        days_overdue = (today - invoice.due_date).days
    elif (invoice.due_date - today).days <= 7:
        status = "due_soon"
        days_overdue = 0
    else:
        status = "upcoming"
        days_overdue = 0
    return {
        "id": invoice.invoice_number,
        "invoiceId": invoice.id,
        "customer": invoice.customer_name,
        "amount": float(invoice.amount),
        "amountPaid": float(invoice.paid_amount),
        "outstanding": outstanding,
        "dueDate": invoice.due_date.isoformat(),
        "status": status,
        "daysOverdue": days_overdue,
        "rolloverCount": invoice.partial_payments.count() if hasattr(invoice, "partial_payments") else 0,
    }


class TwinView(generics.RetrieveAPIView):
    serializer_class = CashFlowTwinSerializer

    def get_object(self):
        return build_cashflow_twin(self.request.user)


class BalanceSeriesView(generics.ListAPIView):
    serializer_class = ForecastPointSerializer

    def get_queryset(self):
        twin = build_cashflow_twin(self.request.user)
        return ForecastPoint.objects.filter(twin=twin).order_by("date")[:90]

    def list(self, request, *args, **kwargs):
        points = list(self.get_queryset())
        return Response([
            {
                "date": p.date.strftime("%d %b"),
                "balance": None,
                "projected": float(p.projected_balance),
            }
            for p in points
        ])


class SummaryView(generics.GenericAPIView):
    def get(self, request):
        from analytics.engines.forecasting_engine import generate_forecast
        twin = build_cashflow_twin(request.user)
        if not twin.forecasts.exists():
            generate_forecast(twin, days=90)
        forecasts = list(twin.forecasts.order_by("date"))
        first_gap = next((p for p in forecasts if p.liquidity_gap), None)
        return Response({
            "currentBalance": float(twin.current_balance),
            "liquidityGapDate": first_gap.date.strftime("%d %b") if first_gap else "No gap",
            "liquidityGapAmount": float(first_gap.projected_balance) if first_gap else 0,
            "avgMonthlyInflow": float(twin.monthly_income),
            "avgMonthlyOutflow": float(twin.monthly_expenses),
        })


class InvoiceListView(generics.ListAPIView):
    def get(self, request):
        from imports.models import ImportedInvoice
        invoices = ImportedInvoice.objects.filter(import_file__user=request.user).prefetch_related("partial_payments")
        return Response([serialize_invoice_status(i) for i in invoices])


class CashFlowEntryCreateView(generics.CreateAPIView):
    serializer_class = CashFlowEntrySerializer

    def perform_create(self, serializer):
        twin, _ = CashFlowTwin.objects.get_or_create(user=self.request.user)
        serializer.save(twin=twin)
        build_cashflow_twin(self.request.user)


class BuildTwinView(generics.GenericAPIView):
    def post(self, request):
        twin = build_cashflow_twin(request.user)
        try:
            rebuild_twin.delay(twin.pk)
        except Exception:
            rebuild_twin(twin.pk)
        return Response(CashFlowTwinSerializer(twin).data)
