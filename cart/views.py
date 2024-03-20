from django.shortcuts import render, get_object_or_404
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
        return render(request, 'cart_summary.html', {'cart_products':cart_products, 'quantities':quantities, 'totals':totals})
    

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