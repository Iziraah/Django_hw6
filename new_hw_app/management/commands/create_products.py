from new_hw_app.models import Product
import random
from django.core.management.base import BaseCommand



clothing_items = ["Футболка", "Джинсы", "Платье", "Пальто", "Брюки", "Юбка", "Рубашка", "Пуловер",
    "Куртка", "Шорты", "Блузка", "Пиджак", "Свитер", "Парка", "Костюм", "Белье", "Носки", "Кепка",
    "Плащ", "Ботинки",
]

class Command(BaseCommand):
    help = 'Создание товаров (10шт)'
    
    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            name = f'{random.choice(clothing_items)}'
            price = random.randint(1000,50000)
            description = f'Описание{i}'
            quantity = random.randint(1, 46) 

            product = Product.objects.create(name=name, price=price, description=description, quantity=quantity)


            product.save() 
            print(f'Создан товар: {name}')

