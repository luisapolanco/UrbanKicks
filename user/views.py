from django.shortcuts import render, redirect
from .forms import CustomerSignUpFrom, AdmSignUpFrom
from django.views import View
# Create your views here.

class CustomerSignUpView(View):
    def get(self, request):
        form = CustomerSignUpFrom
        return render(request, 'customer_sign_up.html', context={'form':form})
    def post(self, request):
        form = CustomerSignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'customer_sign_up.html', context={'form':form})
    
class AdmSignUpView(View):
    def get(self, request):
        form = AdmSignUpFrom
        return render(request, 'adm_sign_up.html', context={'form':form})
    def post(self, request):
        form = AdmSignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'adm_sign_up.html', context={'form':form})
    