from django.urls import path
from catalog import views as catalog

app_name = 'catalog'

urlpatterns = [
    path('', catalog.catalog, name='mainpage'),
    path('product/', catalog.product, name='product')
]