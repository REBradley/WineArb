# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, resolve
from django.conf.urls import url

from test_plus.test import TestCase

from ...users.tests.factories import UserFactory
from .factories import ReviewFactory


class TestReviewURLs(TestCase):
    def setUp(self):
        self.user = UserFactory(username='bobby')
        self.review = ReviewFactory(id=1)

    #Let's test the homepage, briefly
    def test_home_reverse(self):
        """'reviews:home' should reverse to '/'"""
        self.assertEqual(reverse('homepage'), '/')
    def test_home_resolve(self):
        """'/' should resolve to 'reviews:home'"""
        self.assertEqual(resolve('/').view_name, 'homepage')

    def test_new_review_reverse(self):
        """'reviews:new_review' should reverse to '/new_review/'"""
        self.assertEqual(reverse('reviews:new_review'), '/reviews/new_review/')

    def test_new_review(self):
        """'/new_review/' should resolve to 'reviews:new_review'"""
        self.assertEqual(resolve('/reviews/new_review/').view_name, 'reviews:new_review')

    def test_user_review_list(self):
        """'reviews:user_review_list username' should reverse to '/reviews/review/user/bobby/'"""
        self.assertEqual(self.reverse('reviews:user_review_list', username=self.user.username), '/reviews/review/user/bobby/')

    def test_edit_review_form(self):
        """'reviews:edit_review_form review.id' should reverse to '/reviews/review/user/1/'"""
        self.assertEqual(self.reverse('reviews:edit_review_form', review_id=self.review.id), '/reviews/review/edit/1/')

    def test_edit_review(self):
        """'reviews:edit_review review.id' should reverse to '/reviews/review/review/user/1/'"""
        self.assertEqual(self.reverse('reviews:edit_review', review_id=self.review.id), '/reviews/review/edit_review/1/')

    def test_review_detail(self):
        """'reviews:wine_detail review.id' should reverse to '/reviews/detail/1/'"""
        self.assertEqual(self.reverse('reviews:wine_detail', review_id=self.review.id), '/reviews/detail/1/')

    def test_delete_review(self):
        """'reviews:delete_review review.id' should reverse to '/reviews/review/delete_review/1/'"""
        self.assertEqual(self.reverse('reviews:delete_review', review_id=self.review.id), '/reviews/review/delete_review/1/')
