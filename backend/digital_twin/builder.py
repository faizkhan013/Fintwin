from datetime import date
from decimal import Decimal
from django.db.models import Sum
from imports.models import ImportedInvoice
from .models import CashFlowTwin, CashFlowEntry


def build_cashflow_twin(user):
    twin, _ = CashFlowTwin.objects.get_or_create(user=user)

    # Rebuild system-generated receivable entries so the twin always reflects
    # the latest approved/corrected invoice data without duplicating rows.
    CashFlowEntry.objects.filter(twin=twin, source="invoice").delete()
    invoices = ImportedInvoice.objects.filter(import_file__user=user, import_file__status="approved").select_related("import_file")
    for invoice in invoices:
        outstanding = invoice.outstanding_amount
        if outstanding > 0:
            CashFlowEntry.objects.create(
                twin=twin,
                entry_type="income",
                description=f"Receivable {invoice.invoice_number} - {invoice.customer_name}",
                amount=outstanding,
                expected_date=invoice.due_date,
                actual_date=None,
                recurring=False,
                source="invoice",
            )

    income = CashFlowEntry.objects.filter(twin=twin, entry_type="income").aggregate(v=Sum("amount"))["v"] or Decimal("0")
    expenses = CashFlowEntry.objects.filter(twin=twin, entry_type="expense").aggregate(v=Sum("amount"))["v"] or Decimal("0")

    # Paid invoices are the best available current-cash proxy in the current schema.
    paid_cash = invoices.aggregate(v=Sum("paid_amount"))["v"] or Decimal("0")
    actual_income = CashFlowEntry.objects.filter(twin=twin, entry_type="income", actual_date__isnull=False).aggregate(v=Sum("amount"))["v"] or Decimal("0")
    actual_expense = CashFlowEntry.objects.filter(twin=twin, entry_type="expense", actual_date__isnull=False).aggregate(v=Sum("amount"))["v"] or Decimal("0")
    twin.current_balance = paid_cash + actual_income - actual_expense
    twin.monthly_income = income
    twin.monthly_expenses = expenses
    twin.save(update_fields=["current_balance", "monthly_income", "monthly_expenses", "updated_at"])
    return twin
