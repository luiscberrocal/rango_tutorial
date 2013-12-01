#!/usr/bin/env python
# encoding: utf-8
from django.conf.urls import patterns, include, url
from goalmatrix import views

urlpatterns = patterns('', 
	url(r'^employee/(?P<username>\w*)/$', views.showassignments, name='show_assingments'),
	url(r'^goal-matrix/(?P<username>\w*)/(?P<action>\w*)$', views.manage_goal_matrix, name='manage_goal_matrix'),
	url(r'^goal-matrix/update-goals$', views.update_goals, name='update_goals'),
	url(r'^team/(?P<team_short_name>\w*)/$', views.show_team_employees, name='show_team_employees'))


from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
