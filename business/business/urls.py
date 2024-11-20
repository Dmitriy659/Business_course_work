from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('auth/', include('users.urls')),
    path("admin/", admin.site.urls),
    path('', include('homepage.urls')),
    path('categories/', include('categories.urls')),
    # path('orders/', include('orders.urls')),
    # path('products/', include('products.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
