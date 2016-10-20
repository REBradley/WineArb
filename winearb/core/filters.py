from winearb.reviews.models import Review

import django_filters


class ReviewFilter(django_filters.FilterSet):
    RATING_CHOICES = [
        (None, 'Rating Minimum'),
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
        (10, 'Average Rating (or better)'),
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

    rating = django_filters.ChoiceFilter(lookup_expr='gte',
                                         choices=RATING_CHOICES,
                                         label='Minimum Rating',
                                         help_text="",)
    class Meta:
        model=Review
        fields = ['rating']
