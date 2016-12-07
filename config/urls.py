# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
    url(
        regex=r'^$',
        view=TemplateView.as_view(template_name='homepage.html'),
        name='homepage'
    ),
    url(
        regex=r'^about/$',
        view=TemplateView.as_view(template_name='pages/about.html'),
        name='about'
    ),
    url(
        regex=settings.ADMIN_URL,
        view=admin.site.urls
    ),
    url(
        regex=r'^users/',
        view=include('winearb.users.urls', namespace='users')
    ),
    url(
        regex=r'^accounts/',
        view=include('allauth.urls')
    ),
    url(
        regex=r'^reviews/',
        view=include('winearb.reviews.urls', namespace="reviews")
    ),
    url(
        regex=r'^articles/',
        view=include('winearb.articles.urls', namespace="articles")
    ),
    url(
        regex=r'^industry/',
        view=TemplateView.as_view(template_name='pages/services.html'),
        name='industry'
    ),
    url(
        regex=r'^payments/',
        view=include('djstripe.urls', namespace="djstripe")
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(
            regex=r'^400/$',
            view=default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}
        ),
        url(regex=r'^403/$',
            view=default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}
            ),
        url(regex=r'^404/$',
            view=default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}
            ),
        url(regex=r'^500/$',
            view=default_views.server_error
            ),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(regex=r'^__debug__/',
                view=include(debug_toolbar.urls)
                ),
        ]
