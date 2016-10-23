import factory

from ..models import *
from ...users.tests.factories import UserFactory
from ...reviews.tests.factories import ReviewFactory

import os


class WineImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WineImage

    review = factory.SubFactory(ReviewFactory)
    user = factory.SubFactory(UserFactory)
    shot = factory.django.ImageField(
        from_path= '{}/winearb/media/initial_photos/tour-haut-caussan-label.jpg'.format(str(os.getcwd())),
    )
