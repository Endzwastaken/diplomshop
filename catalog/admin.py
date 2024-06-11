from django.contrib import admin
from catalog.models import Categories, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name', ]}

@admin.register(Products)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name', ]}
