from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from .models import ConsentRecord


class ConsentSerializer(serializers.ModelSerializer):
    data_type = serializers.CharField(source="consent_type", read_only=True)
    status = serializers.SerializerMethodField()
    duration_days = serializers.IntegerField(write_only=True, required=False, min_value=1, max_value=3650)

    class Meta:
        model = ConsentRecord
        fields = [
            "id", "user", "consent_type", "data_type", "purpose", "granted",
            "status", "granted_at", "revoked_at", "expires_at", "duration_days", "created_at",
        ]
        read_only_fields = ["user", "granted", "granted_at", "revoked_at", "expires_at", "created_at", "status"]

    def get_status(self, obj):
        return "active" if obj.is_active else "revoked"

    def create(self, validated_data):
        duration_days = validated_data.pop("duration_days", 90)
        user = self.context["request"].user
        consent_type = validated_data["consent_type"]
        obj, _ = ConsentRecord.objects.update_or_create(
            user=user,
            consent_type=consent_type,
            defaults={
                "purpose": validated_data.get("purpose", ""),
                "granted": True,
                "granted_at": timezone.now(),
                "revoked_at": None,
                "expires_at": timezone.now() + timedelta(days=duration_days),
            },
        )
        return obj
