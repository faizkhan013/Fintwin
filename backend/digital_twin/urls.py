from django.urls import path
from .views import TwinView, CashFlowEntryCreateView, BuildTwinView
urlpatterns = [
    path("", TwinView.as_view()),
    path("entry/", CashFlowEntryCreateView.as_view()),
    path("build/", BuildTwinView.as_view()),
]
