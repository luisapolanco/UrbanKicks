#Creado por Samuel Oviedo
from msilib.schema import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from resources.lang.texts import TEXTS
from .models import Brand, BrandImage, Product, ProductImage
from .forms import BrandForm, BrandImageForm, ProductForm, ProductImageForm
from user.decorators import adm_access_only
from django.utils.decorators import method_decorator
# Create your views here.

class SearchProductView(View):

    def get(self, request):
        query = request.GET.get('search_query')
        results = Product.objects.filter(name__icontains=query)
        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'search_results' : TEXTS['search_results'],
            'results': results,
        }
        return render(request, 'search_products.html', context)

class CreateProductView(View):
    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name='get')
    def get(self, request, *args, **kwargs):
        product_form = ProductForm()
        image_form = ProductImageForm()
        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'product_form': product_form,
            'image_form': image_form,
            'create_new_product': TEXTS['create_new_product']
        }
        return render(request, 'create_product.html', context)

    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name="post")
    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)

        if product_form.is_valid() and image_form.is_valid():
            product_instance = product_form.save()
            images = request.FILES.getlist('image')  
            for image in images:
                ProductImage.objects.create(product=product_instance, image=image)
            return redirect('home')
        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'product_form': product_form,
            'image_form': image_form,
        }
        return render(request, 'create_product.html', context)

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'quantity' : TEXTS['quantity'],
            'price' : TEXTS['price'],
            'description' : TEXTS['description'],
            'brand' : TEXTS['brand'],
            'category' : TEXTS['category'],
            'created_at' : TEXTS['created_at'],
            'add_to_cart' : TEXTS['add_to_cart'],
            'product': product,
        }
        return render(request, 'product_detail.html', context)

class ProductDeleteView(View):
    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name="post")
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return redirect('home')
    
class ProductUpdateView(View):
    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name="get")
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(instance=product)
        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'save_changes' : TEXTS['save_changes'],
            'delete_product' : TEXTS['delete_product'],
            'edit': TEXTS['edit'],
            'delete_confirmation_message': TEXTS['delete_confirmation_message'],
            'form': form,
            'product': product,
        }
        return render(request, 'edit_product.html', context)

    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name="post")
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id) 
        context = {
            'form': form,
            'product': product
        }
        return render(request, 'edit_product.html', context )
    
class CreateBrandView(View):
    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name='get')
    def get(self, request, *args, **kwargs):
        brand_form = BrandForm()
        image_form = BrandImageForm()
        context = {
            'create_brand' : TEXTS['create_brand'],
            'brand_form': brand_form,
            'image_form': image_form
        }
        return render(request, 'create_brand.html', context)

    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name='post')
    def post(self, request, *args, **kwargs):
        brand_form = BrandForm(request.POST)
        image_form = BrandImageForm(request.POST, request.FILES)

        if brand_form.is_valid() and image_form.is_valid():
            brand_instance = brand_form.save()
            images = request.FILES.getlist('image')  
            for image in images:
                BrandImage.objects.create(brand=brand_instance, image=image)
            return redirect('home')

        return render(request, 'create_brand.html', {'brand_form': brand_form, 'image_form': image_form})
    
class BrandProductsView(View):
    def get(self, request, brand_id):
        brand = get_object_or_404(Brand, pk=brand_id)
        products = Product.objects.filter(brand=brand)
        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'brand': brand,
            'products': products
        }
        return render(request, 'brand_products.html', context)

