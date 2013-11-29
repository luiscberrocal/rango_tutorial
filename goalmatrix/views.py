from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.base import View
from goalmatrix.models import Employee, Team
from django.template.context import RequestContext


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
    