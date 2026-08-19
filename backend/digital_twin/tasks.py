from celery import shared_task
from .models import CashFlowTwin
from .builder import build_cashflow_twin
from analytics.engines.forecasting_engine import generate_forecast
from analytics.engines.risk_engine import update_risk_metrics

@shared_task
def rebuild_twin(twin_id):
    twin = CashFlowTwin.objects.get(pk=twin_id)
    twin = build_cashflow_twin(twin.user)
    generate_forecast(twin)
    update_risk_metrics(twin)
    return twin.id
