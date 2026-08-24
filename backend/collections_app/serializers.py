from decimal import Decimal
from rest_framework import serializers
from .models import PartialPayment, CollectionAction


class PartialPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartialPayment
        fields = "__all__"
        read_only_fields = ["created_by", "created_at"]

    def validate(self, attrs):
        invoice = attrs["invoice"]
        amount = Decimal(str(attrs["amount"]))
        outstanding = invoice.outstanding_amount
        if amount <= 0:
            raise serializers.ValidationError({"amount": "Payment must be greater than zero."})
        if amount > outstanding:
            raise serializers.ValidationError({"amount": "Payment exceeds the invoice outstanding amount."})
        if invoice.import_file.user != self.context["request"].user:
            raise serializers.ValidationError({"invoice": "You cannot update this invoice."})
        return attrs


class CollectionActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionAction
        fields = "__all__"
        read_only_fields = ["created_by", "action_date"]

    def validate_invoice(self, invoice):
        if invoice.import_file.user != self.context["request"].user:
            raise serializers.ValidationError("You cannot update this invoice.")
        return invoice
