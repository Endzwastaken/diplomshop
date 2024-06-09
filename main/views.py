from django.shortcuts import render
from catalog.models import Categories

def index(request):
    context = {
        'title': 'Главная',
        'content': 'Здравствуйте! '
                   'Мы рады приветствовать вас на сайте интернет-магазина «Системник»! '
                   'У нас вы можете приобрести компьютеры и комплектующие. '
                   'Так же вы можете собрать конфигурацию комьютера на нашем сайте. Приятных покупок!',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'Данный проект является дипломной работой. В дальнейшем буду улучшать, добавлять новый функционал.'
    }
    return render(request, 'main/about.html', context)