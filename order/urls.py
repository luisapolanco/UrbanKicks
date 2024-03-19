from django.urls import path
from .views import OrderDetail, OrderUpdate, OrderDelete
from .forms import OrderCreate

urlpatterns = [
    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('order/create/', OrderCreate.as_view(), name='order_create'),
    path('order/<int:pk>/update/', OrderUpdate.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', OrderDelete.as_view(), name='order_delete'),
]
