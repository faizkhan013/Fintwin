from rest_framework import serializers
from .models import ProductPriceReference

class ProductPriceReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPriceReference
        fields = "__all__"
