from django.urls import path
from orders import views as orders

app_name = 'orders'

urlpatterns = [
    path('create-order/', orders.create_order, name='create_order'),
]

