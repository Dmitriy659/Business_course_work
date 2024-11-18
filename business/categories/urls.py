from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path('', views.all_categories, name="all_categories"),
    path('create', views.create_category, name="create_category")
]
