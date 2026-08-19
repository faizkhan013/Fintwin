from django.urls import path
from .views import RegisterView, BusinessProfileView
urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("profile/", BusinessProfileView.as_view()),
]
