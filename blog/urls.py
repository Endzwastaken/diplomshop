from django.urls import path

from blog import views as blog

app_name = 'blog'

urlpatterns = [
    path('search/', blog.main, name='search'),
    path('', blog.main, name='mainpage'),
    path('<int:post_id>/', blog.post, name='post'),
]

