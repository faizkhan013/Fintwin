from celery import shared_task
from django.utils import timezone
from datetime import date, timedelta
from .models import ImportFile, ImportedInvoice
from .ocr_service import extract_text_from_image, extract_text_from_pdf
from .parsers import parse_invoice_text

@shared_task
def process_import(import_id):
    try:
        obj = ImportFile.objects.get(pk=import_id)
        obj.status = "processing"
        obj.save(update_fields=["status"])
        path = obj.file.path
        text = ""
        if obj.file_type == "pdf":
            text = extract_text_from_pdf(path)
        elif obj.file_type == "invoice":
            text = extract_text_from_image(path)
        parsed = parse_invoice_text(text) if text else {}
        if parsed.get("invoice_number") and parsed.get("amount"):
            ImportedInvoice.objects.create(
                import_file=obj,
                invoice_number=parsed["invoice_number"],
                customer_name="Needs review",
                invoice_date=date.today(),
                due_date=date.today() + timedelta(days=30),
                amount=parsed["amount"],
                confidence_score=0.60,
            )
        obj.status = "review"
        obj.processed_at = timezone.now()
        obj.save(update_fields=["status", "processed_at"])
        return "review"
    except Exception as exc:
        obj = ImportFile.objects.filter(pk=import_id).first()
        if obj:
            obj.status = "failed"
            obj.error_message = str(exc)
            obj.save(update_fields=["status", "error_message"])
        return "failed"
