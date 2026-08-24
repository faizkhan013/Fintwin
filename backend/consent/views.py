from django.utils import timezone
from rest_framework import generics
from .models import ConsentRecord
from .serializers import ConsentSerializer


class ConsentListCreateView(generics.ListCreateAPIView):
    serializer_class = ConsentSerializer

    def get_queryset(self):
        return ConsentRecord.objects.filter(user=self.request.user).order_by("consent_type")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ConsentRevokeView(generics.UpdateAPIView):
    serializer_class = ConsentSerializer
    http_method_names = ["patch", "put", "post"]

    def get_queryset(self):
        return ConsentRecord.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(granted=False, revoked_at=timezone.now(), expires_at=timezone.now())
