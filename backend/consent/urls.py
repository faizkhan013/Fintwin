from django.urls import path
from .views import ConsentListCreateView, ConsentRevokeView
urlpatterns = [
    path("", ConsentListCreateView.as_view()),
    path("<int:pk>/revoke/", ConsentRevokeView.as_view()),
]
