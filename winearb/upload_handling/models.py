from __future__ import unicode_literals
from datetime import date
import StringIO
import uuid

from django.db import models
from django.core.exceptions import ValidationError

from PIL import Image as Img

from ..users.models import User
from ..reviews.models import Wine, Review

#### Helper Functions ###
def validate_image_size(image):
    file_size = image.file.size
    file_size_in_MB = float(file_size)/float(1024 * 1024)
    megabyte_upload_limit = 2.0
    if file_size > megabyte_upload_limit * 1024 * 1024:
        raise ValidationError(
            "Max file size is %sMB, this is %.2fMB" % (megabyte_upload_limit, file_size_in_MB))

def image_upload_path(instance, filename):
  # To customise the path which the image saves to.
  file_extension = filename.split('.')[-1]
  new_file_name = "%s.%s" % (uuid.uuid4(), file_extension)
  month_year_path = date.today().strftime('%Y/%m/')
  shot_path = month_year_path + new_file_name
  full_path = instance.get_upload_path(shot_path)
  return full_path

### Abstract Image Model ###
class BasicImage(models.Model):
  user = models.ForeignKey(User)
  shot = models.ImageField(upload_to=image_upload_path, validators=[validate_image_size])

  class Meta:
      abstract=True
  def __unicode__(self):
    return "%s" % self.shot



### Concrete Image Models ###
class WineImage(BasicImage):
    wine = models.ForeignKey(Wine, null=True, blank=True, on_delete=models.CASCADE,
                             related_name='wineimages')
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='wineimages')

    def get_upload_path(self, filename):
        return "bottle_shots/%s" % filename


class ProfileImage(BasicImage):

    def get_upload_path(self, filename):
        return "profile_pictures/%s/%s" % (self.user, filename)
