from new_hw_app.models import User  
import random
from django.core.management.base import BaseCommand


russian_cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Нижний Новгород",
    "Казань", "Челябинск", "Омск", "Самара", "Ростов-на-Дону", "Уфа", "Красноярск", "Пермь", "Воронеж",
    "Волгоград",
]

class Command(BaseCommand):
    help = 'Создание пользователей (10шт)'
    
    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            name = f'Пользователь{i}'
            email = f'mail{i}@mail.ru'
            password = f'pass{i}'
            age = random.randint(18, 65) 
            address = f'Адрес пользователя {random.choice(russian_cities)}'

            user = User.objects.create(name=name, email=email, password=password, age=age, address=address)


            user.save() 
            print(f'Создан пользователь: {name}')

