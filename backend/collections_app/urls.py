from django.urls import path
from .views import PartialPaymentCreateView, CollectionActionCreateView, CollectionActionListView

urlpatterns = [
    path("partial-payment/", PartialPaymentCreateView.as_view(), name="partial-payment"),
    path("action/", CollectionActionCreateView.as_view(), name="collection-action"),
    path("follow-up/", CollectionActionCreateView.as_view(), name="collection-follow-up"),
    path("actions/", CollectionActionListView.as_view(), name="collection-actions"),
]
