#!/usr/bin/env python
# encoding: utf-8
from django.conf.urls import patterns, include, url
from rango import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'))

from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
