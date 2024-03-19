from django.shortcuts import render
from .models import Order
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.

class OrderDetail(DetailView):
    model = Order

class OrderUpdate(UpdateView):
    model = Order
    fields = ['order_id', 'customer', 'cart_id', 'date_shipped', 'status']

class OrderDelete(DeleteView):
    model = Order