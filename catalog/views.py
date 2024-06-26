from django.core.paginator import Paginator
from django.shortcuts import render
from catalog.models import Products
from catalog.utils import q_search


def catalog(request, category_slug=None):

    # получаем все данные:
    # какой фильтр, какая страница, есть ли поисковый запрос
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    page = int(request.GET.get('page', 1))
    query = request.GET.get('q', None)

    # если категория все товары, то отображаем все товары
    if category_slug == 'all':
        products = Products.objects.all()
    # если есть поисковый запрос, отображаем результаты поиска
    elif query:
        products = q_search(query)
    # иначе отображаем товар по категории
    else:
        products = Products.objects.filter(category__slug=category_slug)
    # если стоит фильтр по скидке, отображаем товары со скидкой
    if on_sale:
        products = products.filter(discount__gt=0)
    # если стоит фильтр, то отображаем по фильтру
    if order_by and order_by != 'default':
        products = products.order_by(order_by)

    paginator = Paginator(products, 6)
    current_page = paginator.page(page)

    context = {
        'title': 'Каталог',
        'products': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'catalog/catalog.html', context)

def product(request, product_slug):
    # получаем из бд товар по запросу слага этого товара
    product = Products.objects.get(slug=product_slug)

    context = {
        'title': 'product.name',
        'product': product
    }
    return render(request, 'catalog/product.html', context)
