from django.contrib import admin


from .models import Wine, Review, Cluster

class WineAdmin(admin.ModelAdmin):
    model = Wine
    list_display = ('name', 'producer', 'country', 'region','vintage',
                    'dominant_variety', 'category', 'value')
    list_filter = ['country', 'region', 'dominant_variety', 'category']


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('wine', 'rating', 'comment', 'user_name', 'created', 'modified')
    list_filter = ['created', 'user_name']
    search_fields = ['comment']

class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    list_display = ['name', 'get_members']



admin.site.register(Wine, WineAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cluster, ClusterAdmin)
