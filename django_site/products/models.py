from django.db import models


# Создаем базовую модель нашего продукта
class Product(models.Model):
      # и указываем максимальную длину
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True)


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
