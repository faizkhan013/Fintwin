from rest_framework import serializers
from .models import ConsentRecord

class ConsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsentRecord
        fields = "__all__"
        read_only_fields = ["user", "granted_at", "revoked_at", "created_at"]
