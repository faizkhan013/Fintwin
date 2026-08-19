from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import BusinessProfile
from .serializers import RegisterSerializer, BusinessProfileSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class BusinessProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = BusinessProfileSerializer
    def get_object(self):
        return BusinessProfile.objects.get(user=self.request.user)
