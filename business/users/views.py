from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

User = get_user_model()


class RegistrationCreateView(CreateView):
    template_name = 'registration/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage:index')
