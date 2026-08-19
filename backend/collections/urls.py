from django.urls import path
from .views import PartialPaymentCreateView, CollectionActionCreateView, CollectionActionListView
urlpatterns = [
    path("partial-payment/", PartialPaymentCreateView.as_view()),
    path("action/", CollectionActionCreateView.as_view()),
    path("actions/", CollectionActionListView.as_view()),
]
