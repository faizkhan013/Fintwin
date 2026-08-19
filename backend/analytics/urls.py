from django.urls import path
from .views import (
    LoanComparisonView, ShockSimulationView, OpportunityCostView,
    SavingsAdvisorView, RecoveryPlanView, FinancingComparisonView,
    RiskSummaryView,
)
urlpatterns = [
    path("loans/", LoanComparisonView.as_view()),
    path("simulation/", ShockSimulationView.as_view()),
    path("opportunity-cost/", OpportunityCostView.as_view()),
    path("savings/", SavingsAdvisorView.as_view()),
    path("recovery/", RecoveryPlanView.as_view()),
    path("financing/", FinancingComparisonView.as_view()),
    path("risk/", RiskSummaryView.as_view()),
]
