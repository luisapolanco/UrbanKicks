from django.urls import path
from .views import CreateProductView, ProductDeleteView, ProductDetailView, ProductUpdateView, SearchProductView

urlpatterns = [
    path('product/search/', SearchProductView.as_view(), name='search_product'),
    path('product/create/', CreateProductView.as_view(), name='create_product'),
    path('product/<int:product_id>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:product_id>/edit/', ProductUpdateView.as_view(), name='product_edit'),
]
