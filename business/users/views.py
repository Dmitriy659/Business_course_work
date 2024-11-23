from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy

User = get_user_model()


class RegistrationCreateView(CreateView):
    template_name = 'registration/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage:index')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(User, pk=self.kwargs.get('pk'))
        if obj != self.request.user:
            raise PermissionDenied
        return obj

    def get_success_url(self):
        return reverse_lazy('user:profile', kwargs={'pk': self.request.user.pk})
