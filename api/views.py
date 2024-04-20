from django.shortcuts import render
from rest_framework import generics

from api.serializers import ProductSerializer
from product.models import Product

# Create your views here.
class GetListProducts(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()