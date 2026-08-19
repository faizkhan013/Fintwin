from django.utils import timezone
from rest_framework import generics
from .models import ConsentRecord
from .serializers import ConsentSerializer

class ConsentListCreateView(generics.ListCreateAPIView):
    serializer_class = ConsentSerializer
    def get_queryset(self):
        return ConsentRecord.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, granted=True, granted_at=timezone.now())

class ConsentRevokeView(generics.UpdateAPIView):
    serializer_class = ConsentSerializer
    def get_queryset(self):
        return ConsentRecord.objects.filter(user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(granted=False, revoked_at=timezone.now())
