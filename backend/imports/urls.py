from django.urls import path
from .views import ImportFileListCreateView, ImportedInvoiceUpdateView, ApproveImportView
urlpatterns = [
    path("", ImportFileListCreateView.as_view()),
    path("invoice/<int:pk>/", ImportedInvoiceUpdateView.as_view()),
    path("<int:pk>/approve/", ApproveImportView.as_view()),
]
