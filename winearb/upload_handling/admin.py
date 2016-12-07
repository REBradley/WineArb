from django.contrib import admin

from models import WineImage, ArticleImage

class WineImageAdmin(admin.ModelAdmin):
    model = WineImage
    list_display = ['shot', 'review', 'user']

class ArticleImageAdmin(admin.ModelAdmin):
    model = WineImage
    list_display = ['shot',]

admin.site.register(WineImage, WineImageAdmin)
admin.site.register(ArticleImage, ArticleImageAdmin)
