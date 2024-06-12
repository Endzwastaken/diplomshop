from django.contrib import admin
from catalog.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name', ]}
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name', ]}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['quantity', 'discount']
    search_fields = ['name', 'description']
    list_filter = ['category', 'discount', 'price']
    fields = ['image', 'name', 'category', 'slug', 'description', 'quantity', ('price', 'discount')]
