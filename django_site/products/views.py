from django.http import HttpResponse

from django.views import generic
# импортируем нашу модель
from .models import Product


class IndexView(generic.ListView):
  template_name = 'products_list.html'  # подключаем наш Темплейт
  context_object_name = 'products'  # под каким именем передадутся данные в Темплейт
  model = Product  # название Модели


class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product

def index(request):
  return HttpResponse("Hello, world. You're at the products index.")
