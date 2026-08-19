from rest_framework import generics
from rest_framework.response import Response
from .models import CashFlowTwin, CashFlowEntry
from .serializers import CashFlowTwinSerializer, CashFlowEntrySerializer
from .builder import build_cashflow_twin
from .tasks import rebuild_twin

class TwinView(generics.RetrieveAPIView):
    serializer_class = CashFlowTwinSerializer
    def get_object(self):
        twin, _ = CashFlowTwin.objects.get_or_create(user=self.request.user)
        return twin

class CashFlowEntryCreateView(generics.CreateAPIView):
    serializer_class = CashFlowEntrySerializer
    def perform_create(self, serializer):
        twin, _ = CashFlowTwin.objects.get_or_create(user=self.request.user)
        serializer.save(twin=twin)

class BuildTwinView(generics.GenericAPIView):
    def post(self, request):
        twin = build_cashflow_twin(request.user)
        rebuild_twin.delay(twin.pk)
        return Response(CashFlowTwinSerializer(twin).data)
