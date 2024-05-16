from django.urls import path
from .views import TrendAdidasVsNike

urlpatterns = [
    path('api/trends', TrendAdidasVsNike.as_view(), name='api_trend')
]