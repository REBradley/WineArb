from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    model = Article

admin.site.register(Article)
