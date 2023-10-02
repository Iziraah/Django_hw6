from django.contrib import admin
from .models import User, Product, Order
# Register your models here.


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['price', '-quantity']
    # list_filter = ['date_added', 'price']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Описание продукта (name)'
    """Отдельный продукт."""
    # fields = ['name', 'description', 'price', 'image', 'quantity']
    readonly_fields = ['registration_date']
    fieldsets = [
            (
                None,
                {
                    'classes': ['wide'],
                    'fields': ['name'],
            },
        ),
            (
            'Подробности',
                {
                    'classes': ['collapse'],
                    # 'image': 'Фотография товара',
                    'description': 'Категория товара и его подробное описание',
                    'fields': ['image', 'description'],
            },
        ),
            (
                'Бухгалтерия',
                    {
                        'fields': ['price', 'quantity'],
                }
        ),
            # (
            #     'Рейтинг и прочее',
            #         {
            #             'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
            #             'fields': ['rating', 'date_added'],
            #         }
            # ),
            ]
    
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'address', 'registration_date']
    ordering = ['name', '-registration_date']
    # list_filter = ['date_added', 'price']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя пользователя (name)'
    """Отдельный Пользователь."""
    # fields = ['name', 'description', 'price', 'image', 'quantity']
    readonly_fields = ['registration_date']
    fieldsets = [
            (
                None,
                {
                    'classes': ['wide'],
                    'fields': ['name'],
            },
        ),
            (
            'Подробности',
                {
                    'classes': ['collapse'],
                    # 'image': 'Фотография товара',
                    # 'email': 'Категория товара и его подробное описание',
                    # 'age':'Возраст пользователя',
                    # 'address':'Город пользователя',
                    'fields': ['email', 'age', 'address',],
            },
        ),
            (
                'Остальное',
                    {
                        'fields': ['registration_date'],
                }
        ),
    ]
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'total_price']
    ordering = ['customer', '-total_price']
    # list_filter = ['date_added', 'price']
    search_fields = ['customer']
    search_help_text = 'Поиск по полю Имя пользователя (customer)'
    """Отдельный Заказ."""
    # fields = ['name', 'description', 'price', 'image', 'quantity']
    readonly_fields = ['date_ordered']
    fieldsets = [
            (
                None,
                {
                    'classes': ['wide'],
                    'fields': ['customer'],
            },
        ),
            (
            'Подробности',
                {
                    'classes': ['collapse'],
                    # 'image': 'Фотография товара',
                    # 'products': 'Список приобретенных продуктов',
                    # 'total_price':'Общая стоимость заказа',
                    'fields': ['products', 'total_price',],
            },
        ),
            (
                'Остальное',
                    {
                        'fields': ['date_ordered'],
                }
        ),
    ]



admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)

