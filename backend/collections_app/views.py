from rest_framework import generics
from .models import PartialPayment, CollectionAction
from .serializers import PartialPaymentSerializer, CollectionActionSerializer

class PartialPaymentCreateView(generics.CreateAPIView):
    serializer_class = PartialPaymentSerializer
    def perform_create(self, serializer):
        payment = serializer.save(created_by=self.request.user)
        invoice = payment.invoice
        invoice.paid_amount += payment.amount
        if invoice.paid_amount > invoice.amount:
            from rest_framework.exceptions import ValidationError
            raise ValidationError({"amount": "Payment exceeds invoice amount."})
        invoice.save(update_fields=["paid_amount"])

class CollectionActionCreateView(generics.CreateAPIView):
    serializer_class = CollectionActionSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CollectionActionListView(generics.ListAPIView):
    serializer_class = CollectionActionSerializer
    def get_queryset(self):
        return CollectionAction.objects.filter(invoice__import_file__user=self.request.user).select_related("invoice")
