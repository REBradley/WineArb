# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^$',
        view=views.new_wine,      #add review form
        name='home'
    ),
    url(
        regex=r'^new_review/$',
        view=views.new_review,     #actually add the review
        name='new_review'
    ),
    url(
        regex=r'^review/user/(?P<username>\w+)/$',
        view=views.user_review_list,
        name='user_review_list'
    ),
    url(
        regex=r'^review/edit/(?P<review_id>[0-9]+)/$',
        view=views.edit_review_form,
        name='edit_review_form'
    ),
    url(
        regex=r'^review/edit_review/(?P<review_id>[0-9]+)/$',
        view=views.edit_review,
        name='edit_review'
    ),
    url(
        regex=r'^review/delete_review/(?P<review_id>[0-9]+)/$',
        view=views.delete_review,
        name='delete_review'
    ),
    url(
        regex=r'^detail/(?P<review_id>[0-9]+)/$',
        view=views.wine_detail,
        name='wine_detail'),
]
