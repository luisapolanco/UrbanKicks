from django.urls import path
from .views import CustomerSignUpView, AdmSignUpView, LoginView

urlpatterns = [
    path('user/customer_sign_up', CustomerSignUpView.as_view(), name='customer_sign_up'),
    path('user/adm_sign_up', AdmSignUpView.as_view(), name='adm_sign_up'),
    path('user/login', LoginView.as_view(), name='login'),
]
