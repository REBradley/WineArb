from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.test import Client

from test_plus.test import TestCase

from ...upload_handling.tests.factories import WineImageFactory, test_image
from ...users.tests.factories import UserFactory

from ...reviews.models import Review

from ..views import (
    new_wine,
    new_review,
    edit_review_form,
    edit_review,
    delete_review,
    user_review_list,
    wine_detail,
)


### Test with AuthenticatedUser ###
class Test_Reviews_Views_With_Authenticated_User(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserFactory(username='RobertParker', password='advocate', email='bobby@wa.com')
        self.client.login(username='RobertParker', password='advocate', email='bobby@wa.com')
        self.model = WineImageFactory()
        self.review = self.model.review

    def test_new_wine_authenticated(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_new_review_authenticated(self):
        data = {'comment': 'Sleeper of the Vintage!', 'rating': 20,}
        response = self.client.post(
                                    '/reviews/new_review/',
                                    data=data,
                                    file=test_image
        )
        self.assertEqual(response.status_code, 200)

    def test_edit_review_form_authenticated(self):
        print 'All: ', self.review.id
        response = self.client.get('/reviews/review/edit/', data={'review_id': self.review.id,})
        self.assertEqual(response.status_code, 200)

    def test_edit_review_authenticated(self):
        response = self.client.get('/reviews/review/edit_review/', data={'review_id': self.review.id,})
        self.assertEqual(response.status_code, 200)

    def test_user_review_list_authenticated(self):
        response = self.client.get('/reviews/review/user/', data={'username': self.review.user.username,})
        self.assertEqual(response.status_code, 200)

    def test_wine_detail_authenticated(self):
        response = self.client.get('/reviews/detail/', data={'review_id': self.review.id,})
        self.assertEqual(response.status_code, 200)

    def test_delete_review_authenticated(self):
        response = self.client.get('/reviews/review/delete_review/', data={'review_id': self.review.id,})
        self.assertEqual(response.status_code, 200)


### AnonymousUser Base Class ###
class BaseReviewsTestCaseAnonymousUser(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.model = WineImageFactory()
        self.review = self.model.review
        self.user = AnonymousUser()
        self.authenticated_user = self.model.user


### Test with AnonymousUser ###
class Test_Reviews_Views_With_Anonymous_User(BaseReviewsTestCaseAnonymousUser):

    def test_new_wine_anonymous(self):
        request = self.factory.get('/')
        request.user = self.user
        response = new_wine(request)
        self.assertEqual(response.status_code, 200)

    def test_new_review_anonymous(self):
        request = self.factory.post('/reviews/new_review/', follow=True)
        request.user = self.user
        response = new_review(request)
        self.assertEqual(response.status_code, 302)

    def test_edit_review_form_anonymous(self):
        request = self.factory.get('/reviews/review/edit/', follow=True)
        request.user = self.user
        response = edit_review_form(request, self.review.id)
        self.assertEqual(response.status_code, 302)

    def test_edit_review_anonymous(self):
        request = self.factory.get('/reviews/review/edit_review/', follow=True)
        request.user = self.user
        response = edit_review(request, self.review.id)
        self.assertEqual(response.status_code, 302)

    def test_delete_review_anonymous(self):
        request = self.factory.get('/reviews/review/delete_review/', follow=True)
        request.user = self.user
        response = delete_review(request, self.review.id)
        self.assertEqual(response.status_code, 302)

    def test_user_review_list_anonymous(self):
        request = self.factory.get('/reviews/review/user/', follow=True)
        request.user = self.user
        response = user_review_list(request, username=self.authenticated_user.username)
        self.assertEqual(response.status_code, 200)

    def test_wine_detail_anonymous(self):
        request = self.factory.get('/reviews/detail/', follow=True)
        request.user = self.user
        response = wine_detail(request, review_id=self.review.id)
        self.assertEqual(response.status_code, 200)
