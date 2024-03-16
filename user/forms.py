from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.db import transaction
from django import forms
from .models import User, Cliente, Adm
from django.contrib.auth import get_user_model

User = get_user_model()

class ClienteSignUpFrom(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    Nombre = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_cliente = True
        if commit:
            user.save()
        cliente = Cliente.objects.create(user=user, Nombre = self.cleaned_data.get('Nombre'))
        return user

class AdmSignUpFrom(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())    