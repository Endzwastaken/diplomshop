from django.contrib import admin
from users.models import User

# @admin.register(User)
# class CategoriesAdmin(admin.ModelAdmin):

admin.site.register(User)