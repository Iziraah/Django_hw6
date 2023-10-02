from django.core.management.base import BaseCommand
from random import randint, sample
from new_hw_app.models import User, Product, Order

class Command(BaseCommand):
    help = 'Создание рандомных заказов для пользователей'

    def handle(self, *args, **options):
        users = User.objects.all()
        products = Product.objects.all()

        for user in users:
            selected_products = sample(list(products), randint(1, 5))
            total_price = sum(product.price for product in selected_products)
            order = Order.objects.create(customer=user, total_price=total_price)
            order.products.set(selected_products)

            self.stdout.write(self.style.SUCCESS(f'Created order for user: {user.name}'))