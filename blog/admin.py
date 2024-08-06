from django.contrib import admin
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date', 'birth_place']
    list_editable = ['birth_date', 'birth_place']
    ordering = ['full_name']
    search_fields = ['full_name']
    list_filter = ['full_name', 'birth_place']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'author']
    list_editable = ['author']
    ordering = ['name']
    search_fields = ['name']
    list_filter = ['name', 'author']