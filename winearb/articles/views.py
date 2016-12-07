# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import render

from .models import Article
from .serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer



def ArticleView(request):
    serialized_articles = ArticleSerializer(Article.objects.all(), many=True)
    data = JSONRenderer().render(serialized_articles.data)
    return render(request, 'articles/articles.html', {'data': data})
