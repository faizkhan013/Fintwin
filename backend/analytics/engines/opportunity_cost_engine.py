def calculate_opportunity_cost(invoice_amount, financing_cost, waiting_days, daily_business_loss):
    finance_cost = invoice_amount * financing_cost / 100
    waiting_loss = waiting_days * daily_business_loss
    difference = waiting_loss - finance_cost
    return {
        "financing_cost": round(finance_cost, 2),
        "waiting_loss": round(waiting_loss, 2),
        "difference": round(difference, 2),
        "finance_may_be_better": difference > 0,
    }
