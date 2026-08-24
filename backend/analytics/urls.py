from django.urls import path
from .views import (
    LoanComparisonView, ShockSimulationView, ShockPresetsView, OpportunityCostView,
    SavingsAdvisorView, SurvivabilityView, RecoveryPlanView, FinancingComparisonView,
    RiskSummaryView, ForecastView,
)

urlpatterns = [
    path("forecast/", ForecastView.as_view(), name="forecast"),
    path("loans/", LoanComparisonView.as_view(), name="loans"),
    path("simulate/", ShockSimulationView.as_view(), name="simulate"),
    path("simulate/presets/", ShockPresetsView.as_view(), name="simulate-presets"),
    path("simulation/", ShockSimulationView.as_view(), name="simulation"),
    path("opportunity-cost/", OpportunityCostView.as_view(), name="opportunity-cost"),
    path("savings/", SavingsAdvisorView.as_view(), name="savings"),
    path("survivability/", SurvivabilityView.as_view(), name="survivability"),
    path("recovery/", RecoveryPlanView.as_view(), name="recovery"),
    path("recovery-plan/", RecoveryPlanView.as_view(), name="recovery-plan"),
    path("financing/", FinancingComparisonView.as_view(), name="financing"),
    path("risk/", RiskSummaryView.as_view(), name="risk"),
]
