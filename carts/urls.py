from django.urls import path
from carts import views as carts

app_name = 'carts'

urlpatterns = [
    path('cart_add/', carts.cart_add, name='cart_add'),
    path('cart_change/', carts.cart_change, name='cart_change'),
    path('cart_remove/', carts.cart_remove, name='cart_remove')
]

