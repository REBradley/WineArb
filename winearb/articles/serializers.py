from rest_framework import serializers

from ..upload_handling.serializers import ArticleImageSerializer

class ArticleSerializer(serializers.Serializer):
    main_title = serializers.CharField(max_length=255)
    sub_title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    image = ArticleImageSerializer()
    date = serializers.CharField(max_length=40)
    text = serializers.CharField()
