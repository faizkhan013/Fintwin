from django.conf import settings
from django.db import models
from decimal import Decimal

class ImportFile(models.Model):
    FILE_TYPES = [("invoice", "Invoice"), ("csv", "CSV"), ("excel", "Excel"), ("pdf", "PDF")]
    STATUS = [("uploaded", "Uploaded"), ("processing", "Processing"), ("review", "Needs Review"), ("approved", "Approved"), ("failed", "Failed")]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="imports")
    file = models.FileField(upload_to="imports/")
    file_type = models.CharField(max_length=20, choices=FILE_TYPES)
    status = models.CharField(max_length=20, choices=STATUS, default="uploaded")
    error_message = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.file.name

class ImportedInvoice(models.Model):
    import_file = models.ForeignKey(ImportFile, on_delete=models.CASCADE, related_name="invoices")
    invoice_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=200)
    invoice_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    corrected = models.BooleanField(default=False)
    confidence_score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def outstanding_amount(self):
        return max(self.amount - self.paid_amount, Decimal("0"))

    def __str__(self):
        return self.invoice_number
