from django.shortcuts import render, redirect
from .forms import CustomerSignUpFrom, AdmSignUpFrom, LoginForm
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.urls import reverse
# Create your views here.

class SignUpView(View):
    def get(self, request):
        return render(request, 'registration/sign_up.html')
    
class CustomerSignUpView(View):
    def get(self, request):
        form = CustomerSignUpFrom
        return render(request, 'registration/customer_sign_up.html', context={'form':form})
    def post(self, request):
        form = CustomerSignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'registration/customer_sign_up.html', context={'form':form})
    
class AdmSignUpView(View):
    def get(self, request):
        form = AdmSignUpFrom
        return render(request, 'registration/adm_sign_up.html', context={'form':form})
    def post(self, request):
        form = AdmSignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'registration/adm_sign_up.html', context={'form':form})

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            return reverse('home')

        else: 
            return reverse('login')
