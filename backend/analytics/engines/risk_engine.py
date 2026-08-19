from collections import defaultdict
from decimal import Decimal
from django.db.models import Sum
from imports.models import ImportedInvoice

def calculate_survivable_loss(monthly_income, monthly_expenses, current_balance):
    if monthly_income <= 0:
        return 0
    surplus = monthly_income - monthly_expenses
    if surplus <= 0:
        return 0
    return round(min(max(((current_balance + surplus) / monthly_income) * 100, 0), 100), 2)

def calculate_emergency_savings(monthly_expenses):
    return 3.0 if monthly_expenses > 0 else 0.0

def calculate_delayed_payment_risk(overdue_amount, receivable_amount):
    if receivable_amount <= 0:
        return 0
    return round(min((overdue_amount / receivable_amount) * 100, 100), 2)

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
    overdue = sum((i.outstanding_amount for i in invoices if i.due_date < __import__("datetime").date.today()), Decimal("0"))
    twin.delayed_payment_risk = calculate_delayed_payment_risk(overdue, receivable)
    twin.concentration_risk = calculate_concentration_risk(invoices)
    twin.survivable_loss_percent = calculate_survivable_loss(twin.monthly_income, twin.monthly_expenses, twin.current_balance)
    twin.emergency_savings_percent = calculate_emergency_savings(twin.monthly_expenses)
    twin.liquidity_risk = 100 if twin.monthly_expenses > twin.monthly_income else 0
    twin.save()
    return twin
