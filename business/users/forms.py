from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'company_name', 'business_type', 'role_in_company')


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'company_name', 'business_type', 'role_in_company')
