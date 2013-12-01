from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.base import View
from goalmatrix.models import Employee, Team, Goal
from django.template.context import RequestContext
import re
from django.http.response import HttpResponse
from django.core.urlresolvers import reverse



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
    if request.method == 'POST':
        message = update_goals(request)
        context_dict.update({'message' : message})
        
    return render_to_response('goalmatrix/goal-matrix-form.html', context_dict, context)

def update_goals(request):
    pattern = re.compile('grade-(\d*)$', re.UNICODE)
    goal_ids = {}
    for key, value in request.POST.iteritems():
        m = pattern.match(key)
        if m:
            goal_ids.update({m.group(1):value})
    goals = Goal.objects.filter(id__in = goal_ids.keys())
    c=0
    for goal in goals:
        uni_goal_id = unicode(goal.id)
        if goal.grade != goal_ids[uni_goal_id]:
            c += 1
            goal.grade = goal_ids[uni_goal_id]
            goal.save()
    
            
    
    #goal_ids.append(('url', request.build_absolute_uri()))
    #return HttpResponse(goal_ids)
    #return manage_goal_matrix(request, request.POST.get('username'), 'edit', message=goal_ids)
    return "Updated %d goals (%s)" % (c , goal_ids.keys())
            
            
            
