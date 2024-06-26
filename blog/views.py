from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Posts


def main(request):
    # получаем все данные:
    page = int(request.GET.get('page', 1))
    posts = Posts.objects.all()
    # пагинация страницы, делим страницу с товарами по 6 товаров на странице
    paginator = Paginator(posts, 6)
    current_page = paginator.page(page)

    context = {
        'title': 'Каталог',
        'posts': current_page,
    }
    return render(request, 'blog/blog.html', context)

def post(request, post_id):
    # получаем из бд товар по запросу слага этого товара
    post = Posts.objects.get(id=post_id)

    context = {
        'title': 'product.name',
        'post': post
    }
    return render(request, 'blog/post.html', context)