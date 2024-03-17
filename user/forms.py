from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.db import transaction
from django import forms
from .models import User, Customer, Adm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomerSignUpFrom(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    name = forms.CharField(widget=forms.TextInput())
    city = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())

    payment_info = forms.CharField(widget=forms.TextInput())
    customer_id = forms.IntegerField(widget=forms.NumberInput())

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'name', 'city', 'address', 'phone_number', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        cliente = Customer.objects.create(user=user, payment_info = self.cleaned_data.get('payment_info'), customer_id = self.cleaned_data.get('customer_id'))
        return user

class AdmSignUpFrom(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    name = forms.CharField(widget=forms.TextInput())
    city = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())

    adm_id = forms.IntegerField(widget=forms.NumberInput())

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'name', 'city', 'address', 'phone_number', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_adm = True
        if commit:
            user.save()
        adm = Adm.objects.create(user=user, adm_id = self.cleaned_data.get('adm_id'))
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())