from decimal import Decimal
from rest_framework import serializers

def non_negative_decimal(value):
    if Decimal(str(value)) < 0:
        raise serializers.ValidationError("Value cannot be negative.")
