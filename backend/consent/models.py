from django.conf import settings
from django.db import models

class ConsentRecord(models.Model):
    CONSENT_TYPES = [
        ("invoice", "Invoice Data"), ("receivable", "Receivable Data"),
        ("expense", "Expense Data"), ("payment", "Payment History"),
        ("bank", "Bank Data"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="consents")
    consent_type = models.CharField(max_length=30, choices=CONSENT_TYPES)
    granted = models.BooleanField(default=False)
    purpose = models.TextField()
    granted_at = models.DateTimeField(null=True, blank=True)
    revoked_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "consent_type")

    def __str__(self):
        return f"{self.user.username} - {self.consent_type}"
