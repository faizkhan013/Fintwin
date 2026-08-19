from django.contrib.auth.models import User
from django.db import models

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="business_profile")
    business_name = models.CharField(max_length=200)
    business_type = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    gst_number = models.CharField(max_length=20, blank=True)
    monthly_revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    monthly_fixed_expenses = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name
