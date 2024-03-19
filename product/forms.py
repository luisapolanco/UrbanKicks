from django import forms
from .models import Brand, BrandImage, Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'brand', 'category']

class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(label='Imagen', required=True, widget=forms.FileInput(attrs={'multiple': True}))
    class Meta:
        model = ProductImage
        fields = ['image']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class BrandImageForm(forms.ModelForm):
    class Meta:
        model = BrandImage
        fields = ['image']
