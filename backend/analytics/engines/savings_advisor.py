def recommend_emergency_savings(monthly_expenses):
    if monthly_expenses <= 0:
        return {"recommended_months": 0, "recommended_amount": 0}
    months = 3
    return {
        "recommended_months": months,
        "recommended_amount": round(monthly_expenses * months, 2),
        "explanation": "Build a reserve covering approximately three months of essential expenses.",
    }
