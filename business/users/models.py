from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, verbose_name="Логин")
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, verbose_name="Имя", blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=True, verbose_name="Фамилия", help_text="Необязательное поле")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    company_name = models.CharField(max_length=30, blank=True, null=True,
                                    help_text="Необязательное поле")
    business_type = models.CharField(max_length=30, blank=False, null=False,
                                     choices=[('Производство', 'Производство'),
                                              ('Торговля', 'Торговля'),
                                              ('ИТ', 'ИТ'),
                                              ('Финансы', 'Финансы'),
                                              ('Здравоохранение', 'Здравоохранение'),
                                              ('Медиа', 'Медиа'),
                                              ('Другое', 'Другое')],
                                     default='Другое')
    role_in_company = models.CharField(max_length=30, blank=True, null=True,
                                       help_text="Необязательное поле")
    registration_date = models.DateField(auto_now_add=True)
    total_revenue = models.PositiveIntegerField(verbose_name='Выручка', default=0)
    total_expenses = models.IntegerField(verbose_name='Затраты', default=0)

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
