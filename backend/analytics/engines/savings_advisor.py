def recommend_emergency_savings(monthly_expenses):
    monthly_expenses = float(monthly_expenses or 0)
    if monthly_expenses <= 0:
        return {
            "recommendedPct": 0,
            "recommendedMonths": 0,
            "recommendedAmount": 0,
            "inflowVolatility": "N/A",
            "reasoning": "Add expense history to estimate a reserve target.",
        }
    months = 3
    amount = monthly_expenses * months
    return {
        "recommendedPct": 15,
        "recommendedMonths": months,
        "recommendedAmount": round(amount, 2),
        "inflowVolatility": "Calculated from available cash-flow history",
        "reasoning": "A three-month essential-expense reserve is used as a conservative planning baseline. The percentage is a budgeting suggestion, not a lending decision.",
    }
