from django.urls import path
from catalog import views as catalog

app_name = 'catalog'

urlpatterns = [
    path('', catalog.catalog, name='mainpage'),
    path('product/<slug:product_slug>/', catalog.product, name='product')
]