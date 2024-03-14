from django.views.generic import View
from product.models import Product
from django.shortcuts import render

# Create your views here.

class HomeView(View):

    def get(self, request):
        newest_products = self.get_newest_products() 
        return render(request, 'home.html', {'newest_products': newest_products})
    
    def get_newest_products(self):
        return Product.objects.order_by('-created_at')[:5]




