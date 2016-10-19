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



    #url(r'^wine/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),



    url(r'^wine$', views.wine_list, name='wine_list'),
    url(r'^recommendation/$', views.user_reccommendation_list, name = 'user_recommendation_list'),
]
