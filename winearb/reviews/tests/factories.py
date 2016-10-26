import random

import factory

from ..models import Review, Wine
from ...users.tests.factories import UserFactory

class WineFactory(factory.django.DjangoModelFactory):
    vintage = 1991
    name = "Finca Dofi"
    producer = 'Alvaro Palacios'
    country = 'Spain'
    region = 'Catalonia'
    appellation = 'Priotat'
    dominant_variety = 'Grenache'
    secondary_variety = 'Cabernet Sauvignon'
    value = 120.00
    category = 'R'
    abv = 14.00

    class Meta:
        model = Wine

class ReviewFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    comment = 'Vintage of the century. Sleeper of the vintage.'
    rating = random.randint(1, 20)

    class Meta:
        model = Review
