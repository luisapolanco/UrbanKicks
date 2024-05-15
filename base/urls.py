#Creado por Samuel Oviedo
from django.urls import path
from .views import HomeView
from .views import MostrarCollaresView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('collares/', MostrarCollaresView.as_view(), name='mostrar-collares'),
]
