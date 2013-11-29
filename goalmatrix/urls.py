#!/usr/bin/env python
# encoding: utf-8
from django.conf.urls import patterns, include, url
from goalmatrix import views

urlpatterns = patterns('', 
	url(r'^employee/(?P<company_id>\d{7})/$', views.showassignments, name='show_assingments'),
	url(r'^team/(?P<team_short_name>\w*)/$', views.show_team_employees, name='show_team_employees'))


from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
