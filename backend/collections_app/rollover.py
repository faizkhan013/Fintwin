from decimal import Decimal

def calculate_rollover(invoice_amount, paid_amount):
    return max(Decimal(str(invoice_amount)) - Decimal(str(paid_amount)), Decimal("0"))
