import os
from datetime import date

from django.test import TestCase
from django.core.exceptions import ValidationError

from .factories import WineImageFactory
from ...reviews.models import Review


class TestWineImage(TestCase):
    """We want to test 3 things:

    1) Assert no images above 2MB are uploaded
    2) Assert we are able to predict the image's url
    3) Assert deleting a review will not affect the existence of the image
    """
    media_url = os.environ.get('MEDIA_URL')
    valid_label = WineImageFactory()
    valid_label_review = Review.objects.get(pk=valid_label.review.id)

    def test_valid_image_size(self):
        self.assertLessEqual(
            self.valid_label.shot.size,
            2 * 1024 * 1024
        )
    def test_large_image_size_validation(self):
        self.assertRaises(ValidationError, WineImageFactory)

    def test_image_url(self):
        wine_part  = 'bottle_shots/'
        date_part = date.today().strftime('%Y/%m/')
        predicted_url_beginning = self.media_url + wine_part + date_part
        self.assertIn(
            predicted_url_beginning,
            self.valid_label.shot.url
        )
    def test_wine_image_stays_when_review_deleted(self):
        self.valid_label_review.delete()
        self.assertIsNotNone(self.valid_label)
