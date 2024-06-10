from django.core.paginator import Paginator
from django.shortcuts import render
from catalog.models import Products


def catalog(request, category_slug):

    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    page = int(request.GET.get('page', 1))

    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        products = products.filter(discount__gt=0)

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
    product = Products.objects.get(slug=product_slug)

    context = {
        'title': 'product.name',
        'product': product
    }
    return render(request, 'catalog/product.html', context)
