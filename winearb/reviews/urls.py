from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.review_list, name='review_list'),
    url(r'^$', views.new_wine, name='home'),
    url(r'^new_review/$', views.new_review, name='new_review'),
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/edit/(?P<review_id>[0-9]+)/$', views.edit_review_form, name='edit_review_form'),
    url(r'^review/edit_review/(?P<review_id>[0-9]+)/$', views.edit_review, name='edit_review'),
    url(r'^review/delete_review/(?P<review_id>[0-9]+)/$', views.delete_review, name='delete_review'),
    url(r'^detail/(?P<review_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),
]
