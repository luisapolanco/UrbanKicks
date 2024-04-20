from django.urls import path
from . import views

urlpatterns = [
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
]
