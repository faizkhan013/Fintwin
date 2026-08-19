from rest_framework import serializers
from .models import PartialPayment, CollectionAction

class PartialPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartialPayment
        fields = "__all__"
        read_only_fields = ["created_by", "created_at"]

class CollectionActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionAction
        fields = "__all__"
        read_only_fields = ["created_by", "action_date"]
