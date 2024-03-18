from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Product
from .forms import ProductForm
from user.decorators import adm_access_only
from django.utils.decorators import method_decorator
# Create your views here.

class SearchProductView(View):

    def get(self, request):
        query = request.GET.get('search_query')
        results = Product.objects.filter(name__icontains=query)
        return render(request, 'search_products.html', {'results': results})

class CreateProductView(View):
    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name='get')
    def get(self, request):
        form = ProductForm()
        return render(request, 'create_product.html', {'form': form})

    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name="post")
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
        return render(request, 'create_product.html', {'form': form})

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'product_detail.html', {'product': product})

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
        return render(request, 'edit_product.html', {'form': form, 'product': product})

    @method_decorator(adm_access_only("No estas autorizado para acceder a la pagina de admin, logeate como admin"), name="post")
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)  # Redirige a la página de detalles del producto editado
        return render(request, 'edit_product.html', {'form': form, 'product': product})

