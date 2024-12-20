from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 10})
        }
