from django import forms
from .models import Product
# class ProductForm(forms.Form):
#     name=forms.CharField(max_length=100)
#     file=forms.FileField()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'file']