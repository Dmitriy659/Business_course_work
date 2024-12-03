import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from products.models import Product

User = get_user_model()


class Order(models.Model):
    buyer = models.CharField(max_length=30, verbose_name='Покупатель', blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created = models.DateField(default=datetime.date.today, verbose_name='Дата покупки', blank=True, null=False)
    delivery = models.CharField(max_length=30, verbose_name='Способ доставки', blank=True,
                                help_text="Укажите способ доставки")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product')
    product_name = models.CharField(max_length=40, verbose_name='Название товара', blank=False, null=False, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], default=0.01,
                                verbose_name='Цена')
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    class Meta:
        verbose_name = 'Позиция в заказе'
        verbose_name_plural = 'Позиции в заказах'

    def __str__(self):
        return f'Позициця в заказе {self.order.id}'
