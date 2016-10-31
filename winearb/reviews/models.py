from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from winearb.core.models import TimeStampedModel
from ..users.models import User


@python_2_unicode_compatible
class Wine(models.Model):
    """Our representation of a wine."""

    vintage = models.PositiveIntegerField(default=3000)
    name = models.CharField(max_length=200, default='New Wine!')
    producer = models.CharField(max_length=50, default='New Wine!')
    country = models.CharField(max_length=50, default='')
    region = models.CharField(max_length=50, default='')
    appellation = models.CharField(max_length=50, default ='')
    dominant_variety = models.CharField(max_length=50, default='')
    secondary_variety = models.CharField(max_length=50, default='', blank=True)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    CATEGORY_CHOICES = [
        ('R', 'Red'),
        ('W', 'White'),
        ('P', 'Rose'),
        ('S', 'Sparkling'),
        ('F', 'Fortified'),
    ]
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default = ' ')
    abv = models.DecimalField(max_digits=4, decimal_places=2, default=14)

    def __str__(self):
        return '%s %s %s' % (self.producer, self.name, self.vintage)

@python_2_unicode_compatible
class Review(TimeStampedModel):
    """A wine review.

    Stores a reference to:
        The contributing user
        Their comment on the particular wine
        Their numerical rating for the wine

    Wine information is to be entered by admin after the review is submitted.
    """
    RATING_CHOICES = [
        (20, '20'),
        (19, '19'),
        (18, '18'),
        (17, '17'),
        (16, '16'),
        (15, 'I would buy (again)'),
        (14, '14'),
        (13, '13'),
        (12, '12'),
        (11, '11'),
        (10, 'Average Rating'),
        (9, '9'),
        (8, '8'),
        (7, '7'),
        (6, '6'),
        (5, 'Not good'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]
    wine = models.ForeignKey(Wine, blank=True, null=True)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=999)
    rating = models.IntegerField(choices=RATING_CHOICES, default=10)

    def __str__(self):
        return self.user.username + self.created.strftime("%Y-%m-%d %H:%M:%S")
