from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ImportFile, ImportedInvoice
from .serializers import ImportFileSerializer, ImportedInvoiceSerializer
from .tasks import process_import

class ImportFileListCreateView(generics.ListCreateAPIView):
    serializer_class = ImportFileSerializer
    parser_classes = [MultiPartParser, FormParser]
    def get_queryset(self):
        return ImportFile.objects.filter(user=self.request.user).prefetch_related("invoices")
    def perform_create(self, serializer):
        obj = serializer.save(user=self.request.user)
        process_import.delay(obj.pk)

class ImportedInvoiceUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ImportedInvoiceSerializer
    def get_queryset(self):
        return ImportedInvoice.objects.filter(import_file__user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(corrected=True)

class ApproveImportView(generics.UpdateAPIView):
    serializer_class = ImportFileSerializer
    def get_queryset(self):
        return ImportFile.objects.filter(user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(status="approved")
