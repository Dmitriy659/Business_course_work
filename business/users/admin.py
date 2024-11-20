from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


# вывод полей в админку
UserAdmin.fieldsets += (
    ('Extra fields', {'fields': ('company', )}),
)
admin.site.register(MyUser, UserAdmin)

