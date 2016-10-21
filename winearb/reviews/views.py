from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from winearb.users.models import User
from .models import Review, Wine, Cluster
from winearb.upload_handling.models import WineImage
from .forms import ReviewForm, ReviewImageForm
from winearb.core.filters import ReviewFilter

import datetime

from .suggestions import update_clusters

#from django.contrib import auth, contenttypes
#from django.contrib.sessions.middleware import SessionMiddleware
#from django.contrib.auth.middleware import AuthenticationMiddleware, SessionAuthenticationMiddleware

from django.contrib.auth.decorators import login_required

def review_list(request):
    latest_review_list = Review.objects.order_by('-created') [:9]
    context = {'latest_review_list' :latest_review_list}
    return render(request, 'reviews/review_list.html', context)

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

def wine_list(request):
    wine_list = Wine.objects.order_by('-name')
    context = {'wine_list' :wine_list}
    return render (request, 'reviews/wine_list.html', context)



#@login_required
#def add_review(request, wine_id):
    #wine = get_object_or_404(Wine, pk=wine_id)
    #review_form = ReviewForm(request.POST, request.FILES)
    #image_form = ReviewImageForm(request.POST, request.FILES)
    #if review_form.is_valid() and image_form.is_valid():

       # cleaned_rating = review_form.cleaned_data['rating']
       # cleaned_comment = review_form.cleaned_data['comment']
       # user_name = request.user.username
       # review = Review()

        #review.wine = wine
       # review.user_name = user_name
       # review.rating = cleaned_rating
       # review.comment = cleaned_comment
       # review.save()
        #update_clusters()

       # image = WineImage(bottle_shot=request.FILES['bottle_shot']) # Not saved yet
       # image.save()

       # review.bottle_shot = image
       # review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

      #  return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))

  #  return render (request,'reviews/wine_detail.html', {'wine':wine,'form': form})

@login_required
def user_reccommendation_list(request):
    # get request user reviewed wines
    user_reviews = Review.objects.filter(user_name=request.user.username).prefetch_related('wine')
    user_reviews_wine_ids = set(map(lambda x: x.wine.id, user_reviews))

    # get request user cluster name (just the first one right now)
    try:
        user_cluster_name = \
            User.objects.get(username=request.user.username).cluster_set.first().name
    except: #if no cluster has been assigned for a user, update clusters
        update_clusters()
        user_cluster_name = \
            User.objects.get(username=request.user.username).cluster_set.first().name


    #get usernames for other members of the cluster
    user_cluster_other_members = \
        Cluster.objects.get(name=user_cluster_name).users \
            .exclude(username=request.user.username).all()
    other_members_usernames = set(map(lambda x: x.username, user_cluster_other_members))

    #get reviews by those users, excluding wines reviewed by the request user
    other_users_reviews = \
        Review.objects.filter(user_name__in=other_members_usernames) \
            .exclude(wine_id__in=user_reviews_wine_ids)
    other_users_reviews_wine_ids = set(map(lambda x: x.wine.id, other_users_reviews))

    #Then get a wine list excluding the previous IDs, order by rating
    wine_list = sorted(
        list(Wine.objects.filter(id__in=other_users_reviews_wine_ids)),
        key=lambda x: x.average_rating,
        reverse=True

    )

    return render(
        request,
        'reviews/user_recommendation_list.html',
        {'username': request.user.username, 'wine_list': wine_list}
    )


#################
def new_wine(request):
    form = ReviewForm(auto_id='')
    image_form = ReviewImageForm(auto_id='')
    return render(request, 'reviews/home.html', {'form': form, 'image_form': image_form,})

@login_required
def new_review(request):
    """
    Create and save a new Review object. Create and save a new WineImage object.
    """
    submitted_review_form = ReviewForm(request.POST)
    submitted_image_form = ReviewImageForm(files=request.FILES)
    print request.FILES['shot'].size
    if submitted_review_form.is_valid() and submitted_image_form.is_valid():
        new_review = Review()
        new_review.save()

        uploaded_file = submitted_image_form.cleaned_data['shot']
        image = WineImage(shot=uploaded_file,
                          user=request.user,
                          review=new_review)


        rating = submitted_review_form.cleaned_data['rating']
        comment = submitted_review_form.cleaned_data['comment']
        user_name = request.user.username

        new_review.user_name = user_name
        new_review.rating = rating
        new_review.comment = comment

        new_review.save()
        image.save()
        #update_clusters() #INPROGRESS


        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('reviews:home'))

    return render (request,'reviews/home.html', {'form': submitted_review_form, 'image_form': submitted_image_form})


@login_required
def edit_review_form(request, review_id):
    """
    Edit an existing review.
    """
    print review_id, 'JJJJJ'
    submitted_review = get_object_or_404(Review, pk=review_id)
    associated_image = get_object_or_404(WineImage, review=submitted_review)
    review_edit_form = ReviewForm(instance=submitted_review)

    print submitted_review,'submitted_review'

    return render(request,
                  'reviews/edit_review.html',
                  {'form': review_edit_form,
                   'image': associated_image,
                   'review': submitted_review})

@login_required
def edit_review(request, review_id):
        """
        Return a new review object from the ReviewForm and ReviewImageForm.
        """

        submitted_review_form = ReviewForm(request.POST)

        if submitted_review_form.is_valid():
            edited_review = get_object_or_404(Review, pk=review_id)

            edited_review.rating = submitted_review_form.cleaned_data['rating']
            edited_review.comment = submitted_review_form.cleaned_data['comment']

            edited_review.save()

            return HttpResponseRedirect(reverse('reviews:home'))


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
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.prefetch_related(
                                                    'wineimages'
                                                ).filter(
                                                    user_name=username
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

    context = {'latest_review_list':latest_review_list_with_images, 'username':username, 'filter': review_filter}
    return render(request, 'reviews/user_review_list.html', context)


def wine_detail(request, review_id, username=None):
    if not username:
        username = request.user.username
    review = get_object_or_404(Review, pk=review_id)
    wine = review.wine
    image = review.wineimages.get(review=review)
    return render(request, 'reviews/wine_detail.html', {'wine': wine, 'review': review, 'image': image})
