from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from product.models import Product, Brand
from api.serializers import ProductSerializer

class GetListProductsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('products')  

        brand = Brand.objects.create(name='Some Brand')
        Product.objects.create(name='Product 1', description='Description 1', price=10.99, brand=brand)
        Product.objects.create(name='Product 2', description='Description 2', price=19.99, brand=brand)

    def test_get_list_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        products = response.data
        expected_products = Product.objects.all()
        serializer = ProductSerializer(expected_products, many=True)

        self.assertEqual(products, serializer.data)