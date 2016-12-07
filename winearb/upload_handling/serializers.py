from rest_framework import serializers

from .models import ArticleImage

class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ('shot',)
