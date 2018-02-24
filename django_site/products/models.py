from django.db import models


# Создаем базовую модель нашего продукта
class Product(models.Model):
      # и указываем максимальную длину
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    category = models.ForeignKey(
        'Category', on_delete='CASCADE', related_name='products', null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.title
