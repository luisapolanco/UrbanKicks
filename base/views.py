#Creado por Samuel Oviedo
from django.views.generic import View
from product.models import Brand, Product
from django.shortcuts import render
import requests

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
            'cart_text' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'trending' : TEXTS['tendencias'],
            'newest_products': newest_products,
            'all_products': all_products,
            'brands': brands,
        }
        
        return render(request, 'home.html', context)
    
class MostrarCollaresView(View):
    def get(self, request, *args, **kwargs):
        try:
            response = requests.get('http://34.41.71.249:8000/api/collares-creados/')
            response.raise_for_status()  # Lanza una excepción para respuestas no exitosas
            data = response.json()
            collares = data.get('collares_personalizados', [])  # Obtiene la lista de collares o una lista vacía si la clave no existe
        except requests.RequestException as e:
            # Manejo de excepciones
            collares = []
            print(e)
            context = {
                'urban_kicks' : TEXTS['urban_kicks'],
                'logout' : TEXTS['logout'],
                'login' : TEXTS['login'],
                'signup' : TEXTS['signup'],
                'cart_text' : TEXTS['cart'],
                'create_product' : TEXTS['create_product'],
                'create_brand' : TEXTS['create_brand'],
                'created_necklaces':TEXTS['created_necklaces'],
                'ID':TEXTS['ID'],
                'material':TEXTS['material'],
                'color':TEXTS['color'],
                'size':TEXTS['tamaño'],
                'text_color':TEXTS['Color de texto'],
                'font':TEXTS['Fuente'],
                'design':TEXTS['Diseño'],
                'there_are_no_custom_necklaces_available':TEXTS['No hay collares personalizados disponibles'],
                'collares': collares,
                }
        return render(request, 'collares.html', context)


