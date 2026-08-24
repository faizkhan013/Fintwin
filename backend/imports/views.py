from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import ImportFile, ImportedInvoice
from .serializers import ImportFileSerializer, ImportedInvoiceSerializer
from .tasks import process_import


class ImportFileListCreateView(generics.ListCreateAPIView):
    serializer_class = ImportFileSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return ImportFile.objects.filter(user=self.request.user).prefetch_related("invoices").order_by("-uploaded_at")

    def perform_create(self, serializer):
        obj = serializer.save(user=self.request.user)
        try:
            process_import.delay(obj.pk)
        except Exception:
            process_import(obj.pk)


class ImportedInvoiceListView(generics.ListAPIView):
    serializer_class = ImportedInvoiceSerializer

    def get_queryset(self):
        return ImportedInvoice.objects.filter(import_file__user=self.request.user).select_related("import_file").order_by("due_date")


class PendingImportListView(generics.ListAPIView):
    serializer_class = ImportFileSerializer

    def get_queryset(self):
        return ImportFile.objects.filter(user=self.request.user, status="review").prefetch_related("invoices").order_by("uploaded_at")


class ImportedInvoiceUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ImportedInvoiceSerializer

    def get_queryset(self):
        return ImportedInvoice.objects.filter(import_file__user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(corrected=True)


class ApproveImportView(generics.UpdateAPIView):
    serializer_class = ImportFileSerializer
    http_method_names = ["patch", "put", "post"]

    def get_queryset(self):
        return ImportFile.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(status="approved")


class ConfirmImportView(generics.GenericAPIView):
    serializer_class = ImportedInvoiceSerializer

    def post(self, request, pk):
        import_file = ImportFile.objects.filter(pk=pk, user=request.user).first()
        if not import_file:
            return Response({"detail": "Import not found."}, status=status.HTTP_404_NOT_FOUND)
        invoices = list(import_file.invoices.all())
        if not invoices:
            return Response({"detail": "No extracted invoice found."}, status=status.HTTP_400_BAD_REQUEST)
        for invoice in invoices:
            payload = request.data if request.data.get("invoice_number") else None
            if payload:
                serializer = ImportedInvoiceSerializer(invoice, data=payload, partial=True, context={"request": request})
                serializer.is_valid(raise_exception=True)
                serializer.save(corrected=True)
            else:
                invoice.corrected = True
                invoice.save(update_fields=["corrected"])
        import_file.status = "approved"
        import_file.save(update_fields=["status"])
        return Response(ImportFileSerializer(import_file, context={"request": request}).data)
