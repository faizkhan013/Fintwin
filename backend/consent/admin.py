from django.contrib import admin
from .models import ConsentRecord

@admin.register(ConsentRecord)
class ConsentAdmin(admin.ModelAdmin):
    list_display = ("user", "consent_type", "granted", "granted_at", "revoked_at")
    list_filter = ("consent_type", "granted")
