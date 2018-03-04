from django.db import models
from django.urls import reverse

# Создаем базовую модель нашего продукта


class Product(models.Model):
      # и указываем максимальную длину
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    category = models.ForeignKey(
        'Category', on_delete='CASCADE', related_name='products', null=True)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.ForeignKey('Product', on_delete='CASCADE')
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete='CASCADE',  null=True)
