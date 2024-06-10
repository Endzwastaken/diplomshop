from django.urls import path
from catalog import views as catalog

app_name = 'catalog'

urlpatterns = [
    path('<slug:category_slug>/', catalog.catalog, name='mainpage'),
    path('product/<slug:product_slug>/', catalog.product, name='product')
]