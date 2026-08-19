from rest_framework import serializers
from .models import CashFlowTwin, CashFlowEntry, ForecastPoint

class CashFlowEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlowEntry
        fields = "__all__"
        read_only_fields = ["twin", "created_at"]

class ForecastPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastPoint
        fields = "__all__"

class CashFlowTwinSerializer(serializers.ModelSerializer):
    entries = CashFlowEntrySerializer(many=True, read_only=True)
    forecasts = ForecastPointSerializer(many=True, read_only=True)
    class Meta:
        model = CashFlowTwin
        fields = "__all__"
        read_only_fields = ["user", "updated_at"]
