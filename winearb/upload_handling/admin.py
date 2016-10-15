from django.contrib import admin

from models import WineImage

class WineImageAdmin(admin.ModelAdmin):
    model = WineImage
    list_display = ['shot', 'review', 'user']

admin.site.register(WineImage, WineImageAdmin)
