from django.urls import path
from .views import CustomerSignUpView, AdmSignUpView

urlpatterns = [
    path('user/customer_sign_up', CustomerSignUpView.as_view(), name='customer_sign_up'),
    path('user/adm_sign_up', AdmSignUpView.as_view(), name='adm_sign_up'),
]
