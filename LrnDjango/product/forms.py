from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'date_posted',
            'producer',
            'title',
            'description',
            'price',
            'stock'
        ]