from django.shortcuts import render
from django.views import View
from .models import Product

# Create your views here.

class SearchProductView(View):

    def get(self, request):
        query = request.GET.get('search_query')
        results = Product.objects.filter(name__icontains=query)
        return render(request, 'search_products.html', {'results': results})
