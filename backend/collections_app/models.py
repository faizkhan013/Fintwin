from django.conf import settings
from django.db import models
from imports.models import ImportedInvoice

class PartialPayment(models.Model):
    invoice = models.ForeignKey(ImportedInvoice, on_delete=models.CASCADE, related_name="partial_payments")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_date = models.DateField()
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CollectionAction(models.Model):
    ACTION_TYPES = [("reminder", "Reminder"), ("call", "Call"), ("email", "Email"), ("partial_payment", "Partial Payment")]
    invoice = models.ForeignKey(ImportedInvoice, on_delete=models.CASCADE, related_name="collection_actions")
    action_type = models.CharField(max_length=30, choices=ACTION_TYPES)
    notes = models.TextField(blank=True)
    action_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
