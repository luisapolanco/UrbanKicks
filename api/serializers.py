from rest_framework import serializers

from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()

    class Meta: 
        model = Product
        fields = ['product_id', 'name', 'price', 'description', 'brand', 'category', 'created_at']