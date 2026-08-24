from datetime import date, timedelta
from pathlib import Path
from celery import shared_task
from django.utils import timezone
from .models import ImportFile, ImportedInvoice
from .ocr_service import extract_text_from_image, extract_text_from_pdf
from .parsers import parse_invoice_text, parse_structured_file


@shared_task

def process_import(import_id):
    obj = ImportFile.objects.get(pk=import_id)
    try:
        obj.status = "processing"
        obj.error_message = ""
        obj.save(update_fields=["status", "error_message"])

        extension = Path(obj.file.name).suffix.lower()
        parsed_rows = []
        if extension in {".csv", ".json"}:
            with obj.file.open("rb") as fh:
                parsed_rows = parse_structured_file(fh, "json" if extension == ".json" else "csv")
        else:
            text = extract_text_from_pdf(obj.file.path) if extension == ".pdf" else extract_text_from_image(obj.file.path)
            parsed = parse_invoice_text(text) if text else {}
            if parsed.get("invoice_number") or parsed.get("amount"):
                invoice_date = parsed.get("invoice_date") or date.today()
                parsed_rows = [{
                    "invoice_number": parsed.get("invoice_number") or f"OCR-{obj.pk}",
                    "customer_name": parsed.get("customer_name") or "Needs review",
                    "invoice_date": invoice_date,
                    "due_date": parsed.get("due_date") or invoice_date + timedelta(days=30),
                    "amount": parsed.get("amount") or 0,
                    "paid_amount": 0,
                    "confidence_score": 0.60,
                }]

        if not parsed_rows:
            raise ValueError("No invoice rows could be extracted. Please upload a readable invoice, CSV, or JSON file.")

        for row in parsed_rows:
            ImportedInvoice.objects.update_or_create(
                import_file=obj,
                invoice_number=row["invoice_number"],
                defaults=row,
            )
        obj.status = "review"
        obj.processed_at = timezone.now()
        obj.save(update_fields=["status", "processed_at"])
        return "review"
    except Exception as exc:
        obj.status = "failed"
        obj.error_message = str(exc)
        obj.processed_at = timezone.now()
        obj.save(update_fields=["status", "error_message", "processed_at"])
        return "failed"
