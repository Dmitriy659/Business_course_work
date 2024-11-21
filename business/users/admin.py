from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import MyUser

User = get_user_model()


class MyUserAdmin(UserAdmin):
    mdodels = User
    list_display = (
        'email', 'is_active', 'is_staff', 'company_name', 'role_in_company',
        'registration_date')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'business_type')

    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),  # Без заголовка, просто поля
        ('Personal info', {'fields': ('first_name', 'last_name', 'company_name', 'business_type', 'role_in_company')}),
        # С заголовком
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company_name', 'business_type', 'role_in_company')})
    )


admin.site.register(MyUser, MyUserAdmin)
