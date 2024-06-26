from django.db.models import Q
from catalog.models import Products

# функция поиска
def q_search(query):
    # если поисковый запрос целочисленный,
    # пытаемся найти среди идентификаторов товаров
    if query.isdigit() and len(query) <=5:
        return Products.objects.filter(id=int(query))
    # разбиваем поисковый запрос на ключевые слова
    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()
    # ищем вхождения ключевых слов в название и описание
    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)