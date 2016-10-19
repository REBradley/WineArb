from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from . models import Review
from ..upload_handling.models import WineImage


class ReviewImageForm(ModelForm):
    class Meta:
        model = WineImage
        fields = ['shot',]





class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'comment',]
        widgets = {
            'comment': Textarea(attrs=dict(cols=40,
                                           rows=15,
                                           placeholder='Thoughts')),
        }
