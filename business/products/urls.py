from django.urls import path
from .views import (ProductListView, CreateProductView, UpdateProductView, DeleteProductView,
                    HeapProductListView)

app_name = 'products'

urlpatterns = [
    path('<int:category_id>/all_products', ProductListView.as_view(), name='all_products'),
    path('<int:category_id>/create_product', CreateProductView.as_view(), name='create_product'),
    path('<int:category_id>/update_product/<int:pk>', UpdateProductView.as_view(), name='update_product'),
    path('<int:category_id>/delete_product/<int:pk>', DeleteProductView.as_view(), name='delete_product'),
    path('heap_products/<slug:sort>', HeapProductListView.as_view(), name='heap_products')
]
