from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'selling_price', 'amount', 'measure_unit')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 10}),
        }
