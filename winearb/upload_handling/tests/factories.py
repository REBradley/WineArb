import factory

from ..models import *
from ...users.tests.factories import UserFactory
from ...reviews.tests.factories import ReviewFactory

### For grabbing a test image. ###
import requests
from PIL import Image
from io import BytesIO

def test_image():
    get_wine_label = requests.get('https://thewinecountry.com/twcwp/wp-content/uploads/2015/04/chateau-margaux-1982-margaux-bordeaux-300x300.jpg')
    image_file = BytesIO(get_wine_label.content)
    return image_file


class WineImageFactory(factory.django.DjangoModelFactory):
    """
    Test the creation of WineImages. Specifically, we want to make sure that this
    is properly loaded onto Amazon S3. Therefore, it needs to be able to run on our production server.
    """
    class Meta:
        model = WineImage

    review = factory.SubFactory(ReviewFactory)
    user = factory.SubFactory(UserFactory)
    shot = factory.django.ImageField(
        from_file=test_image(),
    )
