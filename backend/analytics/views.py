from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShockSimulationSerializer, OpportunityCostSerializer
from .engines.simulation_engine import simulate_shock
from .engines.loan_comparator import compare_loans
from .engines.opportunity_cost_engine import calculate_opportunity_cost
from .engines.savings_advisor import recommend_emergency_savings
from .engines.recovery_planner import create_recovery_plan

class LoanComparisonView(APIView):
    def get(self, request):
        return Response(compare_loans(
            float(request.query_params.get("amount", 100000)),
            int(request.query_params.get("months", 12))
        ))

class ShockSimulationView(APIView):
    def post(self, request):
        serializer = ShockSimulationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(simulate_shock(**serializer.validated_data))

class OpportunityCostView(APIView):
    def post(self, request):
        serializer = OpportunityCostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(calculate_opportunity_cost(**serializer.validated_data))

class SavingsAdvisorView(APIView):
    def get(self, request):
        expenses = float(request.query_params.get("monthly_expenses", 0))
        return Response(recommend_emergency_savings(expenses))

class RecoveryPlanView(APIView):
    def post(self, request):
        return Response(create_recovery_plan(
            float(request.data.get("overdue_amount", 0)),
            float(request.data.get("monthly_surplus", 0))
        ))

class FinancingComparisonView(APIView):
    def post(self, request):
        from .engines.financing_comparator import compare_financing
        return Response(compare_financing(
            float(request.data.get("required_amount", 0)),
            float(request.data.get("financing_cost", 0)),
            float(request.data.get("monthly_cash_gap", 0)),
        ))

class RiskSummaryView(APIView):
    def get(self, request):
        from digital_twin.models import CashFlowTwin
        from .engines.risk_engine import update_risk_metrics
        twin, _ = CashFlowTwin.objects.get_or_create(user=request.user)
        twin = update_risk_metrics(twin)
        return Response({
            "delayed_payment_risk": twin.delayed_payment_risk,
            "concentration_risk": twin.concentration_risk,
            "liquidity_risk": twin.liquidity_risk,
            "survivable_loss_percent": twin.survivable_loss_percent,
            "emergency_savings_months": twin.emergency_savings_percent,
        })
