from django.shortcuts import render
from catalog.models import Categories

def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Главная',
        'content': 'Здравствуйте! '
                   'Мы рады приветствовать вас на сайте интернет-магазина «Системник»! '
                   'У нас вы можете приобрести компьютеры, комплектующие и аксессуары к ним. '
                   'Так же вы можете собрать конфигурацию комьютера на нашем сайте. '
                   'Если у вас возникнут вопросы, наши консультанты с радостью помогут вам. Приятных покупок!',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'Данный проект является дипломной работой. В дальнейшем буду улучшать, добавлять новый функционал.'
    }
    return render(request, 'main/about.html', context)