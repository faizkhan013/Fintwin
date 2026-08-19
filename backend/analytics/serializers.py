from rest_framework import serializers

class ShockSimulationSerializer(serializers.Serializer):
    current_balance = serializers.FloatField()
    monthly_income = serializers.FloatField()
    monthly_expenses = serializers.FloatField()
    income_reduction = serializers.FloatField(default=0, min_value=0, max_value=100)
    expense_increase = serializers.FloatField(default=0, min_value=0)
    delay_days = serializers.IntegerField(default=0, min_value=0)

class OpportunityCostSerializer(serializers.Serializer):
    invoice_amount = serializers.FloatField(min_value=0)
    financing_cost = serializers.FloatField(min_value=0)
    waiting_days = serializers.IntegerField(min_value=0)
    daily_business_loss = serializers.FloatField(min_value=0)
