from datetime import date, timedelta
from decimal import Decimal
from django.db.models import Sum
from digital_twin.models import CashFlowEntry, ForecastPoint


def _ml_daily_net_flow(twin):
    """Fit a tiny explainable linear model on actual daily net cash movement.
    Falls back to zero when there is not enough history or sklearn is unavailable.
    """
    actuals = CashFlowEntry.objects.filter(twin=twin, actual_date__isnull=False).order_by("actual_date")
    points = {}
    for entry in actuals:
        sign = Decimal("1") if entry.entry_type == "income" else Decimal("-1")
        points[entry.actual_date] = points.get(entry.actual_date, Decimal("0")) + sign * entry.amount
    if len(points) < 3:
        return Decimal("0"), "baseline"
    try:
        import numpy as np
        from sklearn.linear_model import LinearRegression
        values = list(points.values())[-30:]
        X = np.arange(len(values), dtype=float).reshape(-1, 1)
        y = np.array([float(v) for v in values])
        model = LinearRegression().fit(X, y)
        prediction = float(model.predict([[len(values)]])[0])
        return Decimal(str(prediction)), "linear_regression"
    except Exception:
        values = list(points.values())[-7:]
        return sum(values, Decimal("0")) / Decimal(len(values)), "moving_average"


def generate_forecast(twin, days=90):
    ForecastPoint.objects.filter(twin=twin).delete()
    start = date.today()
    balance = Decimal(str(twin.current_balance or 0))
    entries = {}
    for entry in twin.entries.all():
        if entry.expected_date < start:
            continue
        entries.setdefault(entry.expected_date, {"income": Decimal("0"), "expense": Decimal("0")})
        entries[entry.expected_date][entry.entry_type] += entry.amount

    baseline_in = Decimal(str(twin.monthly_income or 0)) / Decimal("30")
    baseline_out = Decimal(str(twin.monthly_expenses or 0)) / Decimal("30")
    ml_net, _model = _ml_daily_net_flow(twin)
    ml_net = max(min(ml_net, baseline_in), -baseline_out) if (baseline_in or baseline_out) else Decimal("0")
    results = []
    for i in range(days):
        current_date = start + timedelta(days=i)
        scheduled = entries.get(current_date, {"income": Decimal("0"), "expense": Decimal("0")})
        expected_inflow = scheduled["income"] if scheduled["income"] > 0 else baseline_in
        expected_outflow = scheduled["expense"] if scheduled["expense"] > 0 else baseline_out
        balance += expected_inflow - expected_outflow + (ml_net / Decimal("30"))
        results.append(ForecastPoint.objects.create(
            twin=twin,
            date=current_date,
            expected_inflow=expected_inflow,
            expected_outflow=expected_outflow,
            projected_balance=balance,
            liquidity_gap=balance < 0,
        ))
    return results
