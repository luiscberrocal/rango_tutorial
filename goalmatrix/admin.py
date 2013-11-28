from django.contrib import admin
from goalmatrix.models import Employee, Goal, Assignment, AcceptanceCriteria, Deliverable, Team

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ["employee", "position", "goal", "weight"]
    search_fields = ["goal"]

class AssignmentInLine(admin.TabularInline):
    model = Assignment

class AcceptanceCriteriaInLine(admin.TabularInline):
    model = AcceptanceCriteria
    
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [AssignmentInLine]
    
class GoalAdmin(admin.ModelAdmin):
    inlines = [AcceptanceCriteriaInLine]
    
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(AcceptanceCriteria)
admin.site.register(Deliverable)
admin.site.register(Team)

