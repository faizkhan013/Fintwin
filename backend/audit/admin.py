from django.contrib import admin
from .models import AuditLog
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "method", "endpoint", "timestamp")
    readonly_fields = ("user", "action", "method", "endpoint", "ip_address", "timestamp")
