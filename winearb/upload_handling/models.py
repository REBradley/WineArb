from __future__ import unicode_literals, division
from datetime import date
import uuid

from django.db import models
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import pre_save

from ..users.models import User
from ..reviews.models import Wine, Review

#### Helper Functions ###

def validate_image_size(image):
    """Validator: Ensures that image uploads are no greater than 2MB"""
    file_size = image.file.size
    file_size_in_MB = file_size/(1024 * 1024)
    megabyte_upload_limit = 2.0
    if file_size > megabyte_upload_limit * 1024 * 1024:
        raise ValidationError(
            "Max file size is %sMB, this is %.2fMB" % (megabyte_upload_limit, file_size_in_MB))

def image_upload_path(instance, filename):
    """Gives unique name to the uploaded image and a path based on date."""
    file_extension = filename.split('.')[-1]
    new_file_name = "%s.%s" % (uuid.uuid4(), file_extension)
    year_month_path = date.today().strftime('%Y/%m/')
    shot_path = year_month_path + new_file_name
    full_path = instance.get_upload_path(shot_path)
    return full_path


### Abstract Image Model ###

class BasicImage(models.Model):
    """Defines a basic image. Must have a user, and an Image.

    Since validation is not enforced at the db level by django, and I want it to be,
    we will need to override the save method to enforce image size.
    """
    user = models.ForeignKey(User)
    shot = models.ImageField(upload_to=image_upload_path, validators=[validate_image_size])

    def save(self, *args, **kwargs):
        file_size = float(self.shot.size)/float(1024*1024)
        if file_size > 2.0:
            raise ValidationError(
                {'shot': "Max file size is 2.0MB, this is %.2fMB" % file_size,}
            )
        else:
            super(BasicImage, self).save(*args, **kwargs)

    class Meta:
        abstract=True


### Concrete Image Models ###

class WineImage(BasicImage):
    """Defines a wine bottle image.
    It is just like a basic image, but prepends a path that directs it to the proper folder.
    Also: It is associated with a wine, and must be associated with a review.
    """
    wine = models.ForeignKey(Wine, null=True, blank=True, on_delete=models.CASCADE,
                             related_name='wineimages')
    review = models.ForeignKey(Review, models.SET_NULL, null=True,
                               related_name='wineimages')
    def get_upload_path(self, filename):
        return "bottle_shots/%s" % filename


class ArticleImage(BasicImage):
    """Defines an Article image.
    It is just like a basic image, but prepends a path that directs it to the proper folder.
    """

    def get_upload_path(self, filename):
        return "article_images/%s" % filename
