# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, resolve
from django.conf.urls import url

from test_plus.test import TestCase

class TestArticlesURLs(TestCase):
    def test_url_name_mapping_from_root(self):
        url_string = self.reverse('articles:articles')
        self.assertEqual(url_string, '/articles/')
