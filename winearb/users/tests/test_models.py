from test_plus.test import TestCase

from .factories import UserFactory


class TestUser(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user('testuser')

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            'testuser'
        )
    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )
