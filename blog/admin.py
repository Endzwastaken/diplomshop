from django.contrib import admin
from blog.models import Photos, Posts


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ['post']


@admin.register(Posts)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_timestamp']
    search_fields = ['title', 'created_timestamp', 'edited_timestamp',]
    list_filter = ['category', 'created_timestamp', 'edited_timestamp']
    fields = ['title', 'description', 'edited_timestamp', 'content', 'category']
