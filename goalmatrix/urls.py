#!/usr/bin/env python
# encoding: utf-8
from django.conf.urls import patterns, include, url
from goalmatrix import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('', 
	url(r'^employee/(?P<username>\w*)/$', views.showassignments, name='show_assingments'),
	url(r'^goal-matrix/(?P<username>\w*)/(?P<action>\w*)$', views.manage_goal_matrix, name='manage_goal_matrix'),
	url(r'^goal-matrix/update-goals$', views.update_goals, name='update_goals'),
	url(r'^team/(?P<team_short_name>[\w-]*)/$', views.show_team_employees, name='show_team_employees'),
	url(r'^goals/$', views.show_goals, name='show_goals'),
	)
#urlpatterns += i18n_patterns('', url(r'^index/$', 'views.index' , name='index'))


from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
