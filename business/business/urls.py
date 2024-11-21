from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('homepage.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('user/', include('users.urls')),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    # path('orders/', include('orders.urls')),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
