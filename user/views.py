from django.shortcuts import render, redirect
from .forms import CustomerSignUpFrom, AdmSignUpFrom, LoginForm
from django.views import View
from django.contrib.auth import authenticate, login
#from django.contrib.auth import views as auth_views
from .models import User
import json
from cart.cart import Cart
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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('home')
        return render(request, 'registration/adm_sign_up.html', context={'form':form})

class LoginView(View):#auth_views.LoginView)
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                current_user = User.objects.get(id=request.user.id)
                
                saved_cart = current_user.old_cart

                if saved_cart:
                    converted_cart = json.loads(saved_cart)

                    cart = Cart(request)

                    for key,value in converted_cart.items():
                        cart.db_add(product=key, quantity=value)

                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, self.template_name, {'form':form})
