from django.shortcuts import render, redirect
from resources.lang.texts import TEXTS
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
        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'user_register' : TEXTS['user_register'],
            'choose_user_type_message': TEXTS['choose_user_type_message'],
            'client': TEXTS['client'],
            'admin': TEXTS['admin'],
        }
        return render(request, 'registration/sign_up.html', context)
    
class CustomerSignUpView(View):
    def get(self, request):
        form = CustomerSignUpFrom
        context={
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'register_customer_account': TEXTS['register_customer_account'],
            'register': TEXTS['register'],
            'form': form
        }
        return render(request, 'registration/customer_sign_up.html', context)
    
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
        context= {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'register_admin_account': TEXTS['register_admin_account'],
            'register': TEXTS['register'],
            'form':form,
        }
        return render(request, 'registration/adm_sign_up.html', context )
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
        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'enter' : TEXTS['enter'],
            'form':form
        }
        return render(request, self.template_name, context )
    
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
