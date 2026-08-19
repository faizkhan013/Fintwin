from django.contrib import admin
from .models import ImportFile, ImportedInvoice

@admin.register(ImportFile)
class ImportFileAdmin(admin.ModelAdmin):
    list_display = ("file", "user", "file_type", "status", "uploaded_at")
    list_filter = ("file_type", "status")

@admin.register(ImportedInvoice)
class ImportedInvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "customer_name", "amount", "paid_amount", "due_date", "corrected")
    list_filter = ("corrected",)
    search_fields = ("invoice_number", "customer_name")
