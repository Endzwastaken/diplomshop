from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная',
        'content': 'Здравствуйте! '
                   'Мы рады приветствовать вас на сайте интернет-магазина «Системник»! '
                   'У нас вы можете приобрести компьютеры, комплектующие и аксессуары к ним. '
                   'Так же вы можете собрать конфигурацию комьютера на нашем сайте. '
                   'Если у вас возникнут вопросы, наши консультанты с радостью помогут вам. Приятных покупок!',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'Данный проект является дипломной работой. В дальнейшем буду улучшать, добавлять новый функционал.'
    }
    return render(request, 'main/about.html', context)