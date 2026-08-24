from collections import defaultdict
from decimal import Decimal
from datetime import date
from imports.models import ImportedInvoice


def calculate_survivable_loss(monthly_income, monthly_expenses, current_balance):
    monthly_income = float(monthly_income or 0)
    monthly_expenses = float(monthly_expenses or 0)
    current_balance = float(current_balance or 0)
    if monthly_income <= 0:
        return 0
    return round(min(max((current_balance / monthly_income) * 100, 0), 100), 2)


def calculate_emergency_savings(monthly_expenses):
    return 3.0 if float(monthly_expenses or 0) > 0 else 0.0


def calculate_delayed_payment_risk(overdue_amount, receivable_amount):
    if receivable_amount <= 0:
        return 0
    return round(min((float(overdue_amount) / float(receivable_amount)) * 100, 100), 2)


def calculate_concentration_risk(invoice_qs):
    totals = defaultdict(Decimal)
    for inv in invoice_qs:
        totals[inv.customer_name] += inv.outstanding_amount
    total = sum(totals.values(), Decimal("0"))
    if total <= 0:
        return 0
    largest = max(totals.values(), default=Decimal("0"))
    return round(float(largest / total * 100), 2)


def update_risk_metrics(twin):
    invoices = ImportedInvoice.objects.filter(import_file__user=twin.user)
    receivable = sum((i.outstanding_amount for i in invoices), Decimal("0"))
    overdue = sum((i.outstanding_amount for i in invoices if i.due_date < date.today()), Decimal("0"))
    twin.delayed_payment_risk = calculate_delayed_payment_risk(overdue, receivable)
    twin.concentration_risk = calculate_concentration_risk(invoices)
    twin.survivable_loss_percent = calculate_survivable_loss(twin.monthly_income, twin.monthly_expenses, twin.current_balance)
    twin.emergency_savings_percent = calculate_emergency_savings(twin.monthly_expenses)
    if twin.monthly_expenses <= 0:
        twin.liquidity_risk = 0
    else:
        cash_ratio = float(twin.current_balance) / float(twin.monthly_expenses)
        twin.liquidity_risk = round(max(0, min(100, (1 - cash_ratio) * 100)), 2)
    twin.save()
    return twin
