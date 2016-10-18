from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from . models import Review
from ..upload_handling.models import WineImage


class ReviewImageForm(ModelForm):
    class Meta:
        model = WineImage
        fields = ['shot',]


        # Not Working

        error_messages = {
            'shot': {
                'required': _('Please upload a picture of your wine.'),
                'invalid': _('Please upload a valid image file.'),
                'invalid_image': _('Please upload a valid image file.'),
                'missing': _('Please upload a picture of your wine.'),
                'empty': _('Please upload a picture of your wine.'),
            }
        }



class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'comment',]
        widgets = {
            'comment': Textarea(attrs=dict(cols=40,
                                           rows=15,
                                           placeholder='What did you think of this Wine?')),
        }

        #Don't Work
        error_messages = {
            'comment': {
                'required': _('Please Leave A Score'),
                'missing': _('Please Leave A Score'),
                'empty': _('Please Leave A Score'),
            },
            'rating': {
                'required': _('Please Leave A Score'),
                'missing': _('Please Leave A Score'),
                'empty': _('Please Leave A Score'),
            }
        }
