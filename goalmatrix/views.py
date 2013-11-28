from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from goalmatrix.models import Employee
from django.template.context import RequestContext


def showassignments(request, company_id):
    employee = Employee.objects.get(company_id=company_id)
    context = RequestContext(request)
    context_dict = {'employee': employee}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('goalmatrix/employee.html', context_dict, context)
    