from test_plus.test import TestCase
from winearb.users.tests.factories import UserFactory

class TestBasicImage(TestCase):
    user_factory = UserFactory
    def setUp(self):
        self.make_user()
