from django.urls import path
from .views import CreateOrderView, user_products, OrderListView, OrderDeleteView

app_name = 'orders'

urlpatterns = [
    path('api/user-products/', user_products, name='user_products_api'),
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
    path('all_orders/', OrderListView.as_view(), name='all_orders'),
    path('delete_order/<int:pk>', OrderDeleteView.as_view(), name='delete_order')
]
