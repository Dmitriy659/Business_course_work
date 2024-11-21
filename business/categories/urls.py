from django.urls import path
from .views import CreateCategoryView, CategoryListView, UpdateCategoryView, DeleteCategoryView

app_name = "categories"

urlpatterns = [
    path('', CategoryListView.as_view(), name="all_categories"),
    path('create/', CreateCategoryView.as_view(), name="create_category"),
    path('<int:pk>/update/', UpdateCategoryView.as_view(), name="update_category"),
    path('<int:pk>/delete/', DeleteCategoryView.as_view(), name="delete_category")
]
