from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from products.models import Product

User = get_user_model()


class Order(models.Model):
    buyer = models.CharField(max_length=30, verbose_name='Покупатель', blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ №{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], default=0.01,
                                verbose_name='Цена')
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    def get_total_cost(self):
        return self.product.selling_price * self.quantity

    def get_total_profit(self):
        return (self.product.cost_price - self.product.selling_price) * self.quantity
