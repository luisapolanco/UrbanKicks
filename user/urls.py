from django.urls import path
from .views import CustomerSignUpView, AdmSignUpView, LoginView, SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('user/sign_up', SignUpView.as_view(), name='sign_up' ),
    path('user/sign_up/customer_sign_up', CustomerSignUpView.as_view(), name='customer_sign_up'),
    path('user/sign_up/adm_sign_up', AdmSignUpView.as_view(), name='adm_sign_up'),
    path('user/login', LoginView.as_view(), name='login'),
    path('user/logout', LogoutView.as_view(), name='logout'),
]
