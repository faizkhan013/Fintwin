from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from digital_twin.models import CashFlowTwin
from digital_twin.builder import build_cashflow_twin
from .serializers import ShockSimulationSerializer, OpportunityCostSerializer
from .engines.simulation_engine import simulate_shock
from .engines.loan_comparator import compare_loans, load_bank_rates
from .engines.opportunity_cost_engine import calculate_opportunity_cost
from .engines.savings_advisor import recommend_emergency_savings
from .engines.recovery_planner import create_recovery_plan
from .engines.risk_engine import update_risk_metrics
from .engines.forecasting_engine import generate_forecast


def get_twin(user):
    twin = build_cashflow_twin(user)
    if not twin.forecasts.exists():
        generate_forecast(twin, days=90)
    return twin


class ForecastView(APIView):
    def get(self, request):
        twin = get_twin(request.user)
        forecasts = twin.forecasts.order_by("date")[:90]
        return Response({
            "model": "hybrid_cashflow_forecast",
            "horizon_days": len(forecasts),
            "points": [
                {
                    "date": p.date.isoformat(),
                    "expected_inflow": float(p.expected_inflow),
                    "expected_outflow": float(p.expected_outflow),
                    "projected_balance": float(p.projected_balance),
                    "liquidity_gap": p.liquidity_gap,
                } for p in forecasts
            ],
        })


class LoanComparisonView(APIView):
    def get(self, request):
        amount = float(request.query_params.get("amount", 100000))
        months = int(request.query_params.get("months", 12))
        results = compare_loans(amount, months)
        rates = load_bank_rates()
        enriched = []
        for bank, result in zip(rates, results):
            enriched.append({
                "bank": bank["provider"],
                "product": bank.get("product", "Illustrative working-capital facility"),
                "interestRate": float(bank["interest_rate"]),
                "processingFeePct": float(bank.get("processing_fee_pct", 0.5)),
                "tenureMonths": months,
                "interest_cost": result["interest_cost"],
                "total_repayment": result["total_repayment"],
            })
        return Response(enriched)


class ShockPresetsView(APIView):
    def get(self, request):
        return Response([
            {"id": "late_payment", "label": "Largest receivable is delayed by 30 days"},
            {"id": "lost_customer", "label": "Lose 20% of expected revenue"},
            {"id": "expense_spike", "label": "Expenses rise 15% next month"},
        ])


class ShockSimulationView(APIView):
    def post(self, request):
        twin = get_twin(request.user)
        payload = request.data.copy()
        shock_id = payload.get("shockId") or payload.get("shock_id")
        if shock_id:
            payload.update({"current_balance": float(twin.current_balance), "monthly_income": float(twin.monthly_income), "monthly_expenses": float(twin.monthly_expenses), "shock_id": shock_id})
            if shock_id == "late_payment":
                payload["delay_days"] = 30
            elif shock_id == "lost_customer":
                payload["income_reduction"] = 20
            elif shock_id == "expense_spike":
                payload["expense_increase"] = 15
        serializer = ShockSimulationSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        result = simulate_shock(**{k: v for k, v in serializer.validated_data.items() if k != "shock_id"})
        base = list(twin.forecasts.order_by("date")[:90])
        shocked = []
        for point in base:
            shocked_balance = point.projected_balance
            if shock_id == "late_payment" and point.date <= date.today().replace(day=min(date.today().day + 30, 28)):
                shocked_balance -= float(twin.monthly_income) / 30
            elif shock_id == "lost_customer":
                shocked_balance -= float(twin.monthly_income) * 0.20
            elif shock_id == "expense_spike":
                shocked_balance -= float(twin.monthly_expenses) * 0.15
            shocked.append({"date": point.date.strftime("%d %b"), "balance": None, "projected": float(point.projected_balance), "shocked": round(float(shocked_balance), 2)})
        return Response({"result": result, "series": shocked})


class OpportunityCostView(APIView):
    def post(self, request):
        serializer = OpportunityCostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        values = serializer.validated_data
        if not any(values.values()):
            twin = get_twin(request.user)
            amount = float(twin.current_balance or 100000)
            values = {"invoice_amount": amount, "financing_cost": 6.0, "waiting_days": 14, "daily_business_loss": max(float(twin.monthly_expenses) / 30, 0)}
        result = calculate_opportunity_cost(**values)
        return Response({
            "loanOptionCost": result["financing_cost"],
            "waitingCostEstimate": result["waiting_loss"],
            "waitingCostBasis": "Estimated financing cost is compared with the supplied daily business-loss assumption and waiting period.",
            "verdict": "loan_cheaper" if result["finance_may_be_better"] else "waiting_cheaper",
        })


class SavingsAdvisorView(APIView):
    def get(self, request):
        twin = get_twin(request.user)
        return Response(recommend_emergency_savings(float(twin.monthly_expenses)))


class SurvivabilityView(APIView):
    def get(self, request):
        twin = get_twin(request.user)
        monthly_burn = float(twin.monthly_expenses)
        reserve = float(twin.current_balance)
        weekly_burn = monthly_burn / 4.33 if monthly_burn else 0
        weeks = round(reserve / weekly_burn, 1) if weekly_burn else 0
        return Response({
            "survivableLossAmount": round(reserve, 2),
            "survivableWeeks": weeks,
            "reasoning": "Estimated from current cash reserve and average monthly expense burn; it is a planning indicator, not a guarantee.",
        })


class RecoveryPlanView(APIView):
    def get(self, request):
        twin = get_twin(request.user)
        from imports.models import ImportedInvoice
        overdue = sum(float(i.outstanding_amount) for i in ImportedInvoice.objects.filter(import_file__user=request.user, due_date__lt=date.today()))
        return Response(create_recovery_plan(overdue, float(twin.monthly_income - twin.monthly_expenses)))

    def post(self, request):
        return Response(create_recovery_plan(float(request.data.get("overdue_amount", 0)), float(request.data.get("monthly_surplus", 0))))


class FinancingComparisonView(APIView):
    def post(self, request):
        twin = get_twin(request.user)
        required = float(request.data.get("required_amount") or max(float(twin.monthly_expenses - twin.monthly_income), 0))
        cost = float(request.data.get("financing_cost") or 6)
        gap = float(request.data.get("monthly_cash_gap") or max(float(twin.monthly_expenses - twin.monthly_income), 0))
        options = [
            {"option": "Non-debt (owner reserve / grant)", "totalCost": 0, "speed": "Immediate, if available", "notes": "No financing charge. Availability depends on the business's own reserve or eligible grant."},
            {"option": "Invoice financing", "totalCost": round(required * 0.035, 2), "speed": "1–2 days", "notes": "Illustrative fee; tied to eligible receivables. Verify the provider's actual terms."},
            {"option": "Working-capital facility", "totalCost": round(required * cost / 100, 2), "speed": "3–5 days", "notes": "Illustrative cost only. Actual pricing depends on lender assessment."},
        ]
        return Response(options)


class RiskSummaryView(APIView):
    def get(self, request):
        twin = update_risk_metrics(get_twin(request.user))
        flags = []
        if twin.concentration_risk >= 50:
            severity = "high"
        elif twin.concentration_risk >= 25:
            severity = "medium"
        else:
            severity = "low"
        if twin.concentration_risk > 0:
            flags.append({
                "id": "concentration", "type": "Concentration risk", "severity": severity,
                "message": f"Largest customer represents {twin.concentration_risk:.1f}% of outstanding receivables.",
                "reasoning": "A high share of receivables from one customer makes cash flow more sensitive to a single delayed payment.",
                "numbers": {"customerShare": f"{twin.concentration_risk:.1f}%"},
            })
        if twin.delayed_payment_risk > 0:
            flags.append({
                "id": "delayed-payment", "type": "Delayed-payment risk", "severity": "high" if twin.delayed_payment_risk >= 60 else "medium" if twin.delayed_payment_risk >= 20 else "low",
                "message": f"{twin.delayed_payment_risk:.1f}% of outstanding receivables are overdue.",
                "reasoning": "Overdue receivables can create a liquidity gap even when reported revenue looks healthy.",
                "numbers": {"overdueShare": f"{twin.delayed_payment_risk:.1f}%"},
            })
        if twin.liquidity_risk > 0 or any(p.liquidity_gap for p in twin.forecasts.all()):
            flags.append({
                "id": "liquidity", "type": "Liquidity gap", "severity": "high",
                "message": "Projected cash flow falls below zero in at least one forecast period.",
                "reasoning": "Expected outflows exceed expected inflows in the affected period. Use simulation to test corrective actions before choosing financing.",
                "numbers": {"liquidityRisk": f"{twin.liquidity_risk:.1f}%"},
            })
        return Response(flags)
