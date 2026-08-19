import re
from datetime import datetime

def parse_invoice_text(text):
    data = {}
    m = re.search(r"invoice\s*(?:no|number)?\s*[:#-]?\s*([A-Z0-9-]+)", text, re.I)
    if m:
        data["invoice_number"] = m.group(1)
    m = re.search(r"(?:total|amount)\s*[:₹$]?\s*([\d,]+(?:\.\d+)?)", text, re.I)
    if m:
        data["amount"] = float(m.group(1).replace(",", ""))
    return data
