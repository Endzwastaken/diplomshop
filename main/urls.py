from django.urls import path
from main import views as main

app_name = 'main'

urlpatterns = [
    path('', main.index, name='mainpage'),
    path('about/', main.about, name='about')
]