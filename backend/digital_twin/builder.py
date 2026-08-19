from decimal import Decimal
from django.db.models import Sum
from .models import CashFlowTwin, CashFlowEntry

def build_cashflow_twin(user):
    twin, _ = CashFlowTwin.objects.get_or_create(user=user)
    income = CashFlowEntry.objects.filter(twin=twin, entry_type="income").aggregate(v=Sum("amount"))["v"] or Decimal("0")
    expenses = CashFlowEntry.objects.filter(twin=twin, entry_type="expense").aggregate(v=Sum("amount"))["v"] or Decimal("0")
    twin.monthly_income = income
    twin.monthly_expenses = expenses
    twin.save()
    return twin
