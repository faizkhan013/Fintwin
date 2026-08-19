from django.urls import path
from .views import PriceComparisonView, PriceReferenceListCreateView
urlpatterns = [
    path("compare/", PriceComparisonView.as_view()),
    path("references/", PriceReferenceListCreateView.as_view()),
]
