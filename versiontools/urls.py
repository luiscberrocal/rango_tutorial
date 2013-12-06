#!/usr/bin/env python
# encoding: utf-8
from django.conf.urls import patterns, include, url
from versiontools import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('', 
    url(r'^assemblyinfo$', views.show_assemblyinfo, name='show_assemblyinfo'),
    )
#urlpatterns += i18n_patterns('', url(r'^index/$', 'views.index' , name='index'))


from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
