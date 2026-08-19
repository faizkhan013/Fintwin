def simulate_shock(current_balance, monthly_income, monthly_expenses, income_reduction=0, expense_increase=0, delay_days=0):
    adjusted_income = monthly_income * (1 - income_reduction / 100)
    adjusted_expenses = monthly_expenses * (1 + expense_increase / 100)
    monthly_change = adjusted_income - adjusted_expenses
    delay_loss = (adjusted_income / 30) * delay_days
    final_balance = current_balance + monthly_change - delay_loss
    return {
        "adjusted_income": round(adjusted_income, 2),
        "adjusted_expenses": round(adjusted_expenses, 2),
        "delay_loss": round(delay_loss, 2),
        "final_balance": round(final_balance, 2),
        "survives": final_balance >= 0,
    }
