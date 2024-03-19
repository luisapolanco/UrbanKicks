from django.views.generic.edit import CreateView
from .models import Order

class OrderCreate(CreateView):
    model = Order
    fields = ['order_id', 'customer', 'cart_id', 'date_shipped', 'status']