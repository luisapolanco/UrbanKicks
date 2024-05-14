from django.shortcuts import render, get_object_or_404
from resources.lang.texts import TEXTS
from .cart import Cart
from product.models import Product
from django.http import JsonResponse
from django.views import View

# Create your views here.
class CartSummaryView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quantities()
        totals = cart.cart_total()
        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'shopping_cart' : TEXTS['shopping_cart'],
            'shopping_cart_message' : TEXTS['shopping_cart_message'],
            'price' : TEXTS['price'],
            'description' : TEXTS['description'],
            'brand' : TEXTS['brand'],
            'category' : TEXTS['category'],
            'created_at' : TEXTS['created_at'],
            'quantity' : TEXTS['quantity'],
            'update' : TEXTS['update'],
            'delete' : TEXTS['delete'],
            'total' : TEXTS['total'],
            'pay' : TEXTS['pay'],
            'empty_cart_message' : TEXTS['empty_cart_message'],
            'cart_products':cart_products,
            'quantities':quantities,
            'totals':totals,            
        }
        return render(request, 'cart_summary.html', context)
    

class CartAddView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, product_id = product_id)
        cart.add(product=product, quantity=product_quantity)

        cart_quantity = cart.__len__()
        
        return JsonResponse({'quantity': cart_quantity})

class CartDeleteView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)

        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        
        return JsonResponse({'product':product_id})

class CartUpdateView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        cart.update(product=product_id, quantity=product_quantity)

        return JsonResponse({'quantity':product_quantity})