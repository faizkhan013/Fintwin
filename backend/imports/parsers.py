import csv
import json
import re
from datetime import date, datetime, timedelta
from io import TextIOWrapper


def _parse_date(value, fallback=None):
    if not value:
        return fallback or date.today()
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y", "%d-%b-%Y", "%d %b %Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return fallback or date.today()


def _parse_amount(value):
    if value is None:
        return None
    text = str(value).replace("₹", "").replace(",", "").strip()
    try:
        return float(text)
    except ValueError:
        return None


def parse_invoice_text(text):
    data = {}
    patterns = {
        "invoice_number": r"(?:invoice\s*(?:no|number|#)?)\s*[:#-]?\s*([A-Z0-9][A-Z0-9-]*)",
        "customer_name": r"(?:customer|buyer|bill\s*to)\s*[:#-]?\s*([^\n]+)",
        "amount": r"(?:grand\s*total|total|amount)\s*[:₹$]?\s*([\d,]+(?:\.\d+)?)",
        "due_date": r"(?:due\s*date|payment\s*due)\s*[:#-]?\s*([^\n]+)",
        "invoice_date": r"(?:invoice\s*date|date)\s*[:#-]?\s*([^\n]+)",
    }
    for field, pattern in patterns.items():
        match = re.search(pattern, text or "", re.I)
        if not match:
            continue
        value = match.group(1).strip()
        if field == "amount":
            value = _parse_amount(value)
        elif field in {"due_date", "invoice_date"}:
            value = _parse_date(value)
        data[field] = value
    return data


def parse_structured_file(file_obj, file_type):
    file_obj.seek(0)
    if file_type == "json":
        raw = json.load(file_obj)
        rows = raw if isinstance(raw, list) else raw.get("invoices", raw.get("data", [raw]))
    else:
        text = TextIOWrapper(file_obj, encoding="utf-8-sig", errors="ignore")
        rows = list(csv.DictReader(text))
        text.detach()

    parsed = []
    for row in rows:
        row = {str(k).strip().lower().replace(" ", "_"): v for k, v in row.items()}
        invoice_number = row.get("invoice_number") or row.get("invoice_no") or row.get("invoice") or row.get("number")
        customer = row.get("customer_name") or row.get("customer") or row.get("buyer") or "Needs review"
        amount = _parse_amount(row.get("amount") or row.get("total") or row.get("invoice_amount"))
        if not invoice_number and not amount:
            continue
        invoice_date = _parse_date(row.get("invoice_date") or row.get("date"))
        due_date = _parse_date(row.get("due_date"), invoice_date + timedelta(days=30))
        paid_amount = _parse_amount(row.get("paid_amount") or row.get("paid") or 0) or 0
        parsed.append({
            "invoice_number": str(invoice_number or f"IMP-{datetime.now().strftime('%Y%m%d%H%M%S')}-{len(parsed)+1}"),
            "customer_name": str(customer),
            "invoice_date": invoice_date,
            "due_date": due_date,
            "amount": amount or 0,
            "paid_amount": paid_amount,
            "confidence_score": 0.99 if file_type == "json" else 0.95,
        })
    return parsed
