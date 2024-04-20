from django.urls import path
from . import views

urlpatterns = [
    path('api/products', views.GetListProducts.as_view(), name='products')
]