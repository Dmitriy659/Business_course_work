from django.db import models


class Category(models.Model):
    # user = models.ForeignKey(User,
    #                          on_delete=models.CASCADE,  # удаление пользователя удалит категории
    #                          related_name='categories',
    #                          verbose_name='Пользователь',
    #                          db_column="user_id")
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    class Meta:
        # unique_together = ('user', 'title')
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('title', )

    def __str__(self):
        return self.title

