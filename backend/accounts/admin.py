from django.contrib import admin
from .models import BusinessProfile

@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ("business_name", "user", "industry", "monthly_revenue", "created_at")
    search_fields = ("business_name", "user__username", "gst_number")
