from django.conf import settings
from django.db import models

class CashFlowTwin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cashflow_twin")
    current_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    monthly_income = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    monthly_expenses = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    average_collection_days = models.FloatField(default=0)
    concentration_risk = models.FloatField(default=0)
    delayed_payment_risk = models.FloatField(default=0)
    liquidity_risk = models.FloatField(default=0)
    survivable_loss_percent = models.FloatField(default=0)
    emergency_savings_percent = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

class CashFlowEntry(models.Model):
    ENTRY_TYPES = [("income", "Income"), ("expense", "Expense")]
    twin = models.ForeignKey(CashFlowTwin, on_delete=models.CASCADE, related_name="entries")
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPES)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    expected_date = models.DateField()
    actual_date = models.DateField(null=True, blank=True)
    recurring = models.BooleanField(default=False)
    source = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ForecastPoint(models.Model):
    twin = models.ForeignKey(CashFlowTwin, on_delete=models.CASCADE, related_name="forecasts")
    date = models.DateField()
    expected_inflow = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    expected_outflow = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    projected_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    liquidity_gap = models.BooleanField(default=False)
