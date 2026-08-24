from rest_framework import serializers


class ShockSimulationSerializer(serializers.Serializer):
    current_balance = serializers.FloatField(required=False, default=0)
    monthly_income = serializers.FloatField(required=False, default=0)
    monthly_expenses = serializers.FloatField(required=False, default=0)
    income_reduction = serializers.FloatField(default=0, min_value=0, max_value=100)
    expense_increase = serializers.FloatField(default=0, min_value=0)
    delay_days = serializers.IntegerField(default=0, min_value=0)
    shock_id = serializers.CharField(required=False, allow_blank=True)


class OpportunityCostSerializer(serializers.Serializer):
    invoice_amount = serializers.FloatField(required=False, default=0, min_value=0)
    financing_cost = serializers.FloatField(required=False, default=0, min_value=0)
    waiting_days = serializers.IntegerField(required=False, default=0, min_value=0)
    daily_business_loss = serializers.FloatField(required=False, default=0, min_value=0)
