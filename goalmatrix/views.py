from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from goalmatrix.models import Employee, Assignment
from django.template.context import RequestContext


def showassignments(request, company_id):
    employee = Employee.objects.get(company_id=company_id)
    #print "******************     %s        ***************************" % (employee.id)
    #ddd = employee.assignment_set.all()
    ddd = Assignment.objects.filter(employee__id=employee.id)
    context = RequestContext(request)
    
    context_dict = {'employee': employee, 'assignments' : ddd}
    

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('goalmatrix/employee.html', context_dict, context)
    