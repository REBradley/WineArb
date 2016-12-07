from __future__ import unicode_literals

from django.db import models

from ..upload_handling.models import ArticleImage

class Article(models.Model):
    """Simple article model with basic fields"""
    main_title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Robert Bradley')
    image = models.ForeignKey(ArticleImage)
    date = models.CharField(max_length=40)
    text = models.TextField()

    class Meta:
        verbose_name = 'Article'

    def __unicode__(self):
        return 'Article: %s' % self.main_title
