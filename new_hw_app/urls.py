from django.urls import path, include
from .views import  HelloView, TemplIf, user_orders, add_user, edit_product, product_detail



urlpatterns = [
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('user/<int:user_id>/', user_orders, name='user_orders'),
    path('user/', add_user, name='add_user'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    # path('__debug__/', include("debug_toolbar.urls")),
]

