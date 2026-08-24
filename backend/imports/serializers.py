from pathlib import Path
from rest_framework import serializers
from .models import ImportFile, ImportedInvoice


class ImportedInvoiceSerializer(serializers.ModelSerializer):
    outstanding_amount = serializers.ReadOnlyField()

    class Meta:
        model = ImportedInvoice
        fields = "__all__"
        read_only_fields = ["import_file", "created_at", "outstanding_amount"]

    def validate(self, attrs):
        amount = attrs.get("amount", getattr(self.instance, "amount", 0))
        paid = attrs.get("paid_amount", getattr(self.instance, "paid_amount", 0))
        if paid < 0 or amount < 0:
            raise serializers.ValidationError("Amount values cannot be negative.")
        if paid > amount:
            raise serializers.ValidationError({"paid_amount": "Paid amount cannot exceed invoice amount."})
        return attrs


class ImportFileSerializer(serializers.ModelSerializer):
    invoices = ImportedInvoiceSerializer(many=True, read_only=True)
    file_name = serializers.CharField(source="file.name", read_only=True)

    class Meta:
        model = ImportFile
        fields = "__all__"
        read_only_fields = ["user", "file_type", "status", "error_message", "uploaded_at", "processed_at"]

    def create(self, validated_data):
        file_obj = validated_data["file"]
        ext = Path(file_obj.name).suffix.lower()
        file_type = {".csv": "csv", ".json": "csv", ".xlsx": "excel", ".xls": "excel", ".pdf": "pdf"}.get(ext, "invoice")
        validated_data["file_type"] = file_type
        return super().create(validated_data)
