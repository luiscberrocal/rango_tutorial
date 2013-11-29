from django.contrib import admin
from goalmatrix.models import Employee, Goal, Assignment, AcceptanceCriteria, Deliverable, Team,\
    StandardClassification

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ["employee", "position", "goal", "weight"]
    search_fields = ["goal"]

class AssignmentInLine(admin.TabularInline):
    model = Assignment

class AcceptanceCriteriaInLine(admin.TabularInline):
    model = AcceptanceCriteria

class DeliverableInLine(admin.TabularInline):
    model = Deliverable
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [AssignmentInLine]
    
class GoalAdmin(admin.ModelAdmin):
    list_display = ['position', 'description', 'has_all_acceptance_criteria']
    inlines = [AcceptanceCriteriaInLine, DeliverableInLine]
    
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(AcceptanceCriteria)
admin.site.register(Deliverable)
admin.site.register(Team)
admin.site.register(StandardClassification)

