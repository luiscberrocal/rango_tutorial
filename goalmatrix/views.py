from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.base import View
from goalmatrix.models import Employee, Team
from django.template.context import RequestContext
import re
from django.http.response import HttpResponse



def showassignments(request, username):
    employee = Employee.objects.get(username=username)
    #print "******************     %s        ***************************" % (employee.id)
    #print "******************     %s        ***************************" % (employee.total_assignment)
    context = RequestContext(request)
    
    context_dict = {'employee': employee}

    return render_to_response('goalmatrix/employee.html', context_dict, context)

def show_team_employees(request, team_short_name):
    team = Team.objects.get(short_name=team_short_name.upper())
    context = RequestContext(request)
    context_dict = {'team': team}

    return render_to_response('goalmatrix/team.html', context_dict, context)

def manage_goal_matrix(request, username, action):
    employee = Employee.objects.get(username=username)
    context = RequestContext(request)
    context_dict = {'employee': employee}

    return render_to_response('goalmatrix/goal-matrix-form.html', context_dict, context)

def update_goals(request):
    pattern = re.compile('grade-(\d*)$', re.UNICODE)
    goal_ids = []
    if request.method == 'POST':
        for key, value in request.POST.iteritems():
            m = pattern.match(key)
            if m:
                goal_ids.append((m.group(1), value))
    goal_ids.append(('url', request.build_absolute_uri()))
    return HttpResponse(goal_ids)
            
            
            
