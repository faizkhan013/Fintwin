from django.urls import path
from .views import (
    ImportFileListCreateView, ImportedInvoiceListView, PendingImportListView,
    ImportedInvoiceUpdateView, ApproveImportView, ConfirmImportView,
)

urlpatterns = [
    path("", ImportFileListCreateView.as_view(), name="imports"),
    path("upload/", ImportFileListCreateView.as_view(), name="imports-upload"),
    path("invoices/", ImportedInvoiceListView.as_view(), name="imported-invoices"),
    path("pending/", PendingImportListView.as_view(), name="pending-imports"),
    path("invoice/<int:pk>/", ImportedInvoiceUpdateView.as_view(), name="invoice-update"),
    path("<int:pk>/confirm/", ConfirmImportView.as_view(), name="import-confirm"),
    path("<int:pk>/approve/", ApproveImportView.as_view(), name="import-approve"),
]
