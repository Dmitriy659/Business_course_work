from django.urls import path, include
from .views import RegistrationCreateView

app_name = "user"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', RegistrationCreateView.as_view(), name='registration')
]
