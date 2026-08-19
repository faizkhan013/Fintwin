from datetime import date, timedelta
from decimal import Decimal
from digital_twin.models import ForecastPoint

def generate_forecast(twin, days=90):
    ForecastPoint.objects.filter(twin=twin).delete()
    balance = Decimal(twin.current_balance)
    daily_income = Decimal(twin.monthly_income) / Decimal("30") if twin.monthly_income else Decimal("0")
    daily_expense = Decimal(twin.monthly_expenses) / Decimal("30") if twin.monthly_expenses else Decimal("0")
    results = []
    for i in range(days):
        current_date = date.today() + timedelta(days=i)
        balance += daily_income - daily_expense
        results.append(ForecastPoint.objects.create(
            twin=twin, date=current_date,
            expected_inflow=daily_income, expected_outflow=daily_expense,
            projected_balance=balance, liquidity_gap=balance < 0
        ))
    return results
