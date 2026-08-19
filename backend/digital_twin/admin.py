from django.contrib import admin
from .models import CashFlowTwin, CashFlowEntry, ForecastPoint
admin.site.register(CashFlowTwin)
admin.site.register(CashFlowEntry)
admin.site.register(ForecastPoint)
