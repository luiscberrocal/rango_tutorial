from django.contrib import admin
from goalmatrix.models import Employee, Goal, Assignment, AcceptanceCriteria, Deliverable

admin.site.register(Employee)
admin.site.register(Goal)
admin.site.register(Assignment)
admin.site.register(AcceptanceCriteria)
admin.site.register(Deliverable)

