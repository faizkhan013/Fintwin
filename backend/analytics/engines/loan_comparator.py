import json
from pathlib import Path

RATE_FILE = Path(__file__).resolve().parent.parent / "data" / "bank_rates.json"

def load_bank_rates():
    with open(RATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def compare_loans(amount, months):
    results = []
    for bank in load_bank_rates():
        rate = float(bank["interest_rate"])
        interest = amount * rate / 100 * months / 12
        results.append({
            "provider": bank["provider"],
            "interest_rate": rate,
            "interest_cost": round(interest, 2),
            "total_repayment": round(amount + interest, 2),
        })
    return sorted(results, key=lambda x: x["total_repayment"])
