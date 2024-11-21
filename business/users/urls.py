from django.urls import path
from .views import RegistrationCreateView

app_name = "user"

urlpatterns = [
    path('registration/', RegistrationCreateView.as_view(), name='registration')
]
