from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from product.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quantities()
    totals = cart.cart_total()
    return render(request, 'cart_summary.html', {'cart_products':cart_products, "quantities":quantities, "totals":totals,})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, product_id = product_id)
        cart.add(product=product, quantity = product_quantity)
        
        cart_quantity = cart.__len__()

        response = JsonResponse({'quantity': cart_quantity})

        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        cart.update(product=product_id, quantity=product_quantity)

        response = JsonResponse({'quantity':product_quantity})
        return response
        #return redirect('cart_summary')