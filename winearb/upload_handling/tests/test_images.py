#from test_plus.test import TestCase
#from winearb.users.tests.factories import UserFactory

#class TestBasicImage(TestCase):
    #user_factory = UserFactory
   # def setUp(self):
        #self.make_user()

from .factories import WineImageFactory
### Only run from deployment server to test s3 upload

a = WineImageFactory
a
