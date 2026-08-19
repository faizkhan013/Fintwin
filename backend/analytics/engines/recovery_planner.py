def create_recovery_plan(overdue_amount, monthly_surplus):
    steps = []
    if overdue_amount > 0:
        steps += [
            {"priority": 1, "action": "Follow up on overdue receivables"},
            {"priority": 2, "action": "Request partial payment where possible"},
        ]
    if monthly_surplus <= 0:
        steps.append({"priority": 3, "action": "Review non-essential expenses"})
    else:
        steps.append({"priority": 3, "action": "Allocate part of monthly surplus toward liquidity reserve"})
    return steps
