from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductPriceReference
from .serializers import ProductPriceReferenceSerializer
from .services import compare_product_price

class PriceReferenceListCreateView(generics.ListCreateAPIView):
    queryset = ProductPriceReference.objects.all()
    serializer_class = ProductPriceReferenceSerializer

class PriceComparisonView(APIView):
    def get(self, request):
        product = request.query_params.get("product", "")
        price = float(request.query_params.get("price", 0))
        return Response(compare_product_price(product, price))
