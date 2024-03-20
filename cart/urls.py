from django.urls import path 
from .views import CartSummaryView, CartAddView, CartDeleteView, CartUpdateView

urlpatterns = [
    path('cart/', CartSummaryView.as_view(), name='cart_summary'),
    path('add/', CartAddView.as_view(), name='cart_add'),
    path('delete/', CartDeleteView.as_view(), name='cart_delete'),
    path('update/', CartUpdateView.as_view(), name='cart_update'),
]
