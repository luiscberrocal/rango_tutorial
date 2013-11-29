from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from goalmatrix.models import Employee, Assignment
from django.template.context import RequestContext


def showassignments(request, company_id):
    employee = Employee.objects.get(company_id=company_id)
    #print "******************     %s        ***************************" % (employee.id)
    print "******************     %s        ***************************" % (employee.total_assignment)
    context = RequestContext(request)
    
    context_dict = {'employee': employee}

    return render_to_response('goalmatrix/employee.html', context_dict, context)
    