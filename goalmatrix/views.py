from django.shortcuts import render_to_response
from goalmatrix.models import Employee, Team, Goal, Assignment
from django.template.context import RequestContext
import re
from decimal import Decimal
from django.utils.translation import ugettext as _
from django.http.response import HttpResponse


def index(request):
    # Translators: This message appears on the home page only
    output = _("No month specified")
    return HttpResponse(output)

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
def show_goals(request):
    goals = Goal.objects.all()
    context = RequestContext(request)
    context_dict = {'goals': goals}
    return render_to_response('goalmatrix/goals.html', context_dict, context)
    
def update_goals(request):
    pattern = re.compile('grade-(\d*)$', re.UNICODE)
    ag_pattern = re.compile('assignment-grade-(\d*)$', re.UNICODE)
    goal_ids = {}
    assignment_ids={}
    for key, value in request.POST.iteritems():
        m = pattern.match(key)
        if m:
            goal_ids.update({m.group(1):value})
        ag_m = ag_pattern.match(key)
        if ag_m:
            assignment_ids.update({ag_m.group(1):value})
    goals = Goal.objects.filter(id__in = goal_ids.keys())
    assignments = Assignment.objects.filter(id__in=assignment_ids.keys())
    goal_count=0
    assignment_count=0
    for goal in goals:
        uni_goal_id = unicode(goal.id)
        #gg = goal.grade
        #ggn = Decimal(goal_ids[uni_goal_id])
        #raise Exception("Ee")
        if goal_ids[uni_goal_id] == u'None' or len(goal_ids[uni_goal_id]) == 0 :
            goal_count += 1
            goal.grade = None
            goal.save()
        else :
            if goal.grade != Decimal(goal_ids[uni_goal_id]):
                goal_count += 1
                goal.grade = goal_ids[uni_goal_id]
                goal.save()
    for assignment in assignments:
        uni_assignment_id = unicode(assignment.id)
        if assignment_ids[uni_assignment_id] == u'None' or len(assignment_ids[uni_assignment_id]) == 0:
            assignment_count += 1
            assignment.grade = None
            assignment.save()
        else :
            if assignment.grade != Decimal(assignment_ids[uni_assignment_id]):
                assignment_count += 1
                assignment.grade = assignment_ids[uni_assignment_id]
                assignment.save()
            
    #goal_ids.append(('url', request.build_absolute_uri()))
    #return HttpResponse(goal_ids)
    #return manage_goal_matrix(request, request.POST.get('username'), 'edit', message=goal_ids)
    return "Updated %d goals, %d assignments" % (goal_count , assignment_count)
            
            
            
