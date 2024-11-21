from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from categories.models import Category

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название товара',
                             blank=False, null=False)
    description = models.TextField(verbose_name='Описание товара')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2,
                                     validators=[MinValueValidator(0.01)],
                                     verbose_name='Себестоимость',
                                     blank=False, null=False)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2,
                                        validators=[MinValueValidator(0.01)],
                                        verbose_name='Цена продажи',
                                        blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 verbose_name='Кол-во', validators=[MinValueValidator(0)],
                                 blank=False, null=False, help_text="Кол-во товара в наличии")
    measure_unit = models.CharField(max_length=15, verbose_name='Единицы измерения', blank=False,
                                    null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    class Meta:
        unique_together = ('title', 'user', 'category')
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('category', 'title',)

    def __str__(self):
        return self.title
