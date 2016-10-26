import requests
from io import BytesIO

import factory

from ..models import *
from ...users.tests.factories import UserFactory
from ...reviews.tests.factories import ReviewFactory

### Variables ###

# First is valid, second is over 3Mb
label_image_list = [
    'https://thewinecountry.com/twcwp/wp-content/uploads/2015/04/chateau-margaux-1982-margaux-bordeaux-300x300.jpg',
    'http://wineandjurisprudence.org/wp-content/uploads/2013/05/sparkling-wine-labels.jpg',
]

def get_test_image(url):
    """Testing utility used to retrieve wine pictures from the internet and convert them into streams."""
    get_wine_label = requests.get(url)
    image_file = BytesIO(get_wine_label.content)
    return image_file


class WineImageFactory(factory.django.DjangoModelFactory):
    """Test the creation of WineImages. Specifically, we want to make sure that the image can be
    properly sent onto Amazon S3. Therefore, it needs to be able to run on our production server,
    as well as locally.
    """
    class Meta:
        model = WineImage

    review = factory.SubFactory(ReviewFactory)
    user = factory.SubFactory(UserFactory)
    shot = factory.django.ImageField(
        from_file=factory.Iterator(label_image_list, getter=lambda c: get_test_image(c)),
    )
