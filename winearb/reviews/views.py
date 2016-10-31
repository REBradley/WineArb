# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from winearb.upload_handling.models import WineImage

from winearb.core.filters import ReviewFilter

from .models import Review
from .forms import ReviewForm, ReviewImageForm
from ..users.models import User


def new_wine(request):
    """Render a wine review form as the view, with 3 fields.
    It is composed of 2 forms: One for the comment and rating,
    the other for a wine image to be uploaded.
    """
    form = ReviewForm(auto_id='')
    image_form = ReviewImageForm(auto_id='')
    return render(request, 'reviews/home.html', {'form': form, 'image_form': image_form,})

@login_required
def new_review(request):
    """Create and save a new Review and an associated WineImage."""

    submitted_review_form = ReviewForm(request.POST)
    submitted_image_form = ReviewImageForm(files=request.FILES)
    user = request.user

    if submitted_review_form.is_valid() and submitted_image_form.is_valid():

        rating = submitted_review_form.cleaned_data['rating']
        comment = submitted_review_form.cleaned_data['comment']
        uploaded_file = submitted_image_form.cleaned_data['shot']

        new_review = Review()
        new_review.user = user
        new_review.rating = rating
        new_review.comment = comment
        new_review.save()

        image = WineImage(
                          shot=uploaded_file,
                          user=user,
                          review=new_review,
        )
        image.save()

        return HttpResponseRedirect(reverse('reviews:home'))
    return render(request,'reviews/home.html', {'form': submitted_review_form, 'image_form': submitted_image_form})

@login_required
def edit_review_form(request, review_id):
    """
    Edit an existing review.
    """
    submitted_review = get_object_or_404(Review, pk=review_id)
    associated_image = get_object_or_404(WineImage, review=submitted_review)
    review_edit_form = ReviewForm(instance=submitted_review)

    return render(request,
                  'reviews/edit_review.html',
                  {'form': review_edit_form,
                   'image': associated_image,
                   'review': submitted_review})

@login_required
def edit_review(request, review_id):
        """Return an updated Review from the ReviewForm data; same WineImage."""
        submitted_review_form = ReviewForm(request.POST)

        if submitted_review_form.is_valid():
            edited_review = get_object_or_404(Review, pk=review_id)

            edited_review.rating = submitted_review_form.cleaned_data['rating']
            edited_review.comment = submitted_review_form.cleaned_data['comment']
            edited_review.save()

            return HttpResponseRedirect(reverse('reviews:home'))
        # If form was invalid, present it again.
        edited_review = get_object_or_404(Review, pk=review_id)
        associated_image = get_object_or_404(WineImage, review=edited_review)
        return render(request,
                      'reviews/edit_review.html',
                      {'form': submitted_review_form,
                       'image': associated_image,
                       'review': edited_review})

@login_required
def delete_review(request, review_id):
    review_to_delete = get_object_or_404(Review, pk=review_id)
    review_to_delete.delete()
    return HttpResponseRedirect(reverse('reviews:home'))

def user_review_list(request, username=None):
    """Displays the given user's list of reviewed wines.

    The wine image, name, and rating given by the user are all displayed.
    There is the option to sort the wine by rating.
    """
    if username:
        user = User.objects.get(username=username)
    else:
        username = request.user.username
        user= request.user
    latest_review_list = Review.objects.prefetch_related(
                                                    'wineimages'
                                                ).filter(
                                                    user=user
                                                ).order_by(
                                                    '-created'
                                                )
    review_filter = ReviewFilter(request.GET, queryset=latest_review_list)

    review_images = list(map(lambda x: x.wineimages.get(review=x), review_filter))
    latest_review_list_with_images = zip(review_filter, review_images)

    paginator = Paginator(latest_review_list_with_images,10)
    page = request.GET.get('page')
    try:
        latest_review_list_with_images = paginator.page(page)
    except PageNotAnInteger:
        latest_review_list_with_images = paginator.page(1)
    except EmptyPage:
        latest_review_list_with_images = paginator.page(paginator.num_pages)

    context = {'latest_review_list':latest_review_list_with_images,
               'username':username,
               'filter': review_filter}
    return render(request, 'reviews/review_list.html', context)

def wine_detail(request, review_id):
    """Detail view of a single wine."""

    review = get_object_or_404(Review, pk=review_id)
    wine = review.wine
    image = review.wineimages.get(review=review)
    return render(request, 'reviews/wine_detail.html', {'wine': wine, 'review': review, 'image': image})
