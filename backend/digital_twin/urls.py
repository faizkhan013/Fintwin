from django.urls import path
from .views import TwinView, CashFlowEntryCreateView, BuildTwinView, BalanceSeriesView, SummaryView, InvoiceListView

urlpatterns = [
    path("", TwinView.as_view(), name="twin"),
    path("entry/", CashFlowEntryCreateView.as_view(), name="twin-entry"),
    path("build/", BuildTwinView.as_view(), name="twin-build"),
    path("rebuild/", BuildTwinView.as_view(), name="twin-rebuild"),
    path("balance-series/", BalanceSeriesView.as_view(), name="balance-series"),
    path("summary/", SummaryView.as_view(), name="twin-summary"),
    path("invoices/", InvoiceListView.as_view(), name="twin-invoices"),
]
