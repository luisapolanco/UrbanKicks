#Creado por Samuel Oviedo
from django.urls import path
from .views import BrandProductsView, CreateBrandView, CreateProductView, ProductDeleteView, ProductDetailView, ProductUpdateView, SearchProductView, CreateReportView

urlpatterns = [
    path('product/search/', SearchProductView.as_view(), name='search_product'),
    path('product/create/', CreateProductView.as_view(), name='create_product'),
    path('brand/create/', CreateBrandView.as_view(), name='create_brand'),
    path('brands/<int:brand_id>/', BrandProductsView.as_view(), name='brand_products'),
    path('product/<int:product_id>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:product_id>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/create_csv', CreateReportView.as_view(), name='create_report'),
]
