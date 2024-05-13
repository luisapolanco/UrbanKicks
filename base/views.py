#Creado por Samuel Oviedo
from django.views.generic import View
from product.models import Brand, Product
from django.shortcuts import render

from resources.lang.texts import TEXTOS
# Create your views here.


class HomeView(View):

    def get(self, request):
        newest_products = Product.objects.order_by('-created_at')[:8]
        all_products = Product.objects.all()
        brands = Brand.objects.all()

        context = {
            'newest_products': newest_products,
            'all_products': all_products,
            'brands': brands,
            'crear_product' : TEXTOS['crear_producto']
        }
        
        return render(request, 'home.html', context)



