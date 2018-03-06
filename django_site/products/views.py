from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# импортируем нашу модель
from .models import Product
from .models import Category
from .models import Order


class IndexView(generic.ListView):
    template_name = 'products_list.html'  # подключаем наш Темплейт
    context_object_name = 'products'  # под каким именем передадутся данные в Темплейт
    model = Product  # название Модели
    paginate_by = 6
    queryset = Product.objects.all()
    # метод для добавления дополнительной информации в контекст

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # передаем в словарь контекста список всех категорий
        context['categories'] = Category.objects.all()
        return context


class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product


class CategoryDetail(generic.DetailView):
    template_name = 'category_detail.html'
    model = Category


class CategoryList(generic.ListView):
    template_name = 'category_list.html'
    context_object_name = 'categorys'
    model = Category


class ProductCreate(generic.CreateView):
    model = Product
    # название нашего шаблона с формой
    template_name = 'product_new.html'
    # какие поля будут в форме
    fields = '__all__'


class OrderFormView(generic.CreateView):
    model = Order
    template_name = 'order_form.html'
    success_url = '/'
    fields = 'customer_name', 'customer_phone'

    def form_valid(self, form):
        product = Product.objects.get(id=self.kwargs['pk'])
        user = self.request.user
        form.instance.user = user
        form.instance.product = product
        return super().form_valid(form)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
