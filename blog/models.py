from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from catalog.models import Categories


class Posts(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True,
                                             verbose_name='Дата создания')
    edited_timestamp = models.DateTimeField(blank=True, null=True,
                                            verbose_name='Дата редактирования')
    description = models.CharField(max_length=150, unique=True,
                                   verbose_name='Описание')
    content = models.TextField(unique=True, verbose_name='Контент')
    title = models.CharField(max_length=50, unique=True,
                             verbose_name='Заголовок')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT,
                                 verbose_name='Категория')

    class Meta:
        db_table = 'post'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['id',]

    def __str__(self):
        return self.title

    def display_content(self):
        return mark_safe(self.content)


class Photos(models.Model):
    post = models.ForeignKey(to=Posts, on_delete=models.PROTECT,
                             verbose_name='Пост')
    image = models.ImageField(upload_to='product_images', blank=True,
                              null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'photo'
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.post

