from django.urls import path
from .views import RegistrationCreateView, UserUpdateView

app_name = "user"

urlpatterns = [
    path('registration/', RegistrationCreateView.as_view(), name='registration'),
    path('profile/<int:pk>', UserUpdateView.as_view(), name='profile')
]
