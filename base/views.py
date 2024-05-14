#Creado por Samuel Oviedo
from django.views.generic import View
from product.models import Brand, Product
from django.shortcuts import render

from resources.lang.texts import TEXTS

class HomeView(View):

    def get(self, request):
        newest_products = Product.objects.order_by('-created_at')[:8]
        all_products = Product.objects.all()
        brands = Brand.objects.all()

        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'newest_products': newest_products,
            'all_products': all_products,
            'brands': brands,
        }
        
        return render(request, 'home.html', context)



