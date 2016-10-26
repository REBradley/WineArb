from django.utils import timezone

from test_plus import TestCase

from .factories import WineFactory, ReviewFactory


class TestWine(TestCase):
    wine = WineFactory()

    def test__str__(self):
        self.assertEqual(
            self.wine.__str__(),
            'Alvaro Palacios Finca Dofi 1991'
        )

class TestReview(TestCase):
    review = ReviewFactory()
    timestamp = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

    def test__str__(self):
        self.assertEqual(
            self.review.__str__(),
            'user-0' + self.timestamp
        )
