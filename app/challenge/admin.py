from django.contrib import admin
from .models import Author, Article
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'additional_information']
    search_fields = ['name']



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'summary', 'content']
    ordering = ['-created_at']
    search_fields = ['title', 'category', 'author__name',]