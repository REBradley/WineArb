from __future__ import unicode_literals, absolute_import

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from config.settings.common import AUTH_USER_MODEL

from ..core.models import TimeStampedModel

import numpy as np

class Wine(models.Model):
    vintage = models.PositiveIntegerField(default=2016)
    name = models.CharField(max_length=200)
    producer = models.CharField(max_length=50, default = ' ')
    country = models.CharField(max_length=50, default = ' ')
    region = models.CharField(max_length=50, default = ' ')
    appellation = models.CharField(max_length=50, default = ' ')
    dominant_variety = models.CharField(max_length=50, default=' ')
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




    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return '%s %s %s' % (self.producer, self.name, self.vintage)

class Review(TimeStampedModel):
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
        (10, 'Average, considering cost'),
        (9, '9'),
        (8, '8'),
        (7, '7'),
        (6, '6'),
        (5, 'Not good at this price'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]

    wine = models.ForeignKey(Wine, blank=True, null=True)
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=10)

    def __str__(self):
        return self.user_name + str(self.created)



class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(AUTH_USER_MODEL)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])
