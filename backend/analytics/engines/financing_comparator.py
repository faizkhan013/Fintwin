def compare_financing(required_amount, financing_cost, monthly_cash_gap=0):
    cost = required_amount * financing_cost / 100
    return {
        "required_amount": round(required_amount, 2),
        "financing_cost": round(cost, 2),
        "net_received": round(required_amount - cost, 2),
        "monthly_cash_gap": round(monthly_cash_gap, 2),
        "decision": "USER_DECIDES",
    }
