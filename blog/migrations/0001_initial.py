# Generated by Django 5.0.6 on 2024-06-24 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_alter_categories_options_alter_products_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edited_timestamp', models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')),
                ('description', models.CharField(max_length=100, unique=True, verbose_name='Описание')),
                ('content', models.TextField(unique=True, verbose_name='Контент')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Заголовок')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'db_table': 'post',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Изображение')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.posts', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
                'db_table': 'photo',
            },
        ),
    ]
