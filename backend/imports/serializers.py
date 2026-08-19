from rest_framework import serializers
from .models import ImportFile, ImportedInvoice

class ImportedInvoiceSerializer(serializers.ModelSerializer):
    outstanding_amount = serializers.ReadOnlyField()
    class Meta:
        model = ImportedInvoice
        fields = "__all__"
        read_only_fields = ["import_file", "created_at", "outstanding_amount"]

class ImportFileSerializer(serializers.ModelSerializer):
    invoices = ImportedInvoiceSerializer(many=True, read_only=True)
    class Meta:
        model = ImportFile
        fields = "__all__"
        read_only_fields = ["user", "status", "error_message", "uploaded_at", "processed_at"]
