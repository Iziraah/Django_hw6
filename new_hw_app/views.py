import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import User, Order, Product
from .forms import UserForm, ProductForm

# Create your views here.
logger = logging.getLogger(__name__)


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")
    
class TemplIf(TemplateView):
    template_name = "new_hw_app/templ_if.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context
    
def user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)  # Получаем пользователя по его id
    orders = Order.objects.filter(customer=user)  # Получаем все заказы этого пользователя
    
    return render(request, 'new_hw_app/user_orders.html', {'user': user, 'orders': orders})
    
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'new_hw_app/user_form.html', {'form':form, 'message': message})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'new_hw_app/edit_product.html', {'form': form, 'product': product})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'new_hw_app/product_detail.html', {'product': product})