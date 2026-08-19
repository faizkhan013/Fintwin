from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BusinessProfile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    business_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "business_name"]

    def create(self, validated_data):
        business_name = validated_data.pop("business_name")
        user = User.objects.create_user(**validated_data)
        BusinessProfile.objects.create(user=user, business_name=business_name)
        return user

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = "__all__"
        read_only_fields = ["user", "created_at", "updated_at"]
