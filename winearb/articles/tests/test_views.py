from django.core.urlresolvers import reverse

from test_plus.test import TestCase


class TestArticlesURLs(TestCase):
    def test_articles_get_200(self):
        response = self.get_check_200('articles:articles')
