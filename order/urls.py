from django.urls import path
from .views import OrderCreate

urlpatterns = [
    path('order/create/', OrderCreate.as_view(), name='order_create'),
]
