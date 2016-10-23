import random
import factory

from ..models import Review

class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    user_name = factory.Sequence(lambda n: 'Robert_Pa%ser' % n)
    comment = 'Vintage of the century. Sleeper of the vintage.'
    rating = random.randint(1,19)
