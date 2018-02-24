from django.http import HttpResponse

from django.views import generic
# импортируем нашу модель
from .models import Product
from .models import Category


class IndexView(generic.ListView):
    template_name = 'products_list.html'  # подключаем наш Темплейт
    context_object_name = 'products'  # под каким именем передадутся данные в Темплейт
    model = Product  # название Модели


class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product


class CategoryDetail(generic.DetailView):
    template_name = 'category_detail.html'
    model = Category
