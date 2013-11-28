from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Team(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    
    def __unicode__(self):
        return u"%s, %s" % (self.short_name, self.name,)

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    company_id = models.CharField(max_length=8,
	    validators=[
	        RegexValidator(
	            regex='^\d{7}$',
	            message='company id must be 7 digits',
	            code='invalid_company_id'
	        ),
	    ])
    team = models.ForeignKey(Team, null=True, blank=True)
    
    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_name,)

class Goal(models.Model):
    position = models.IntegerField()
    description = models.CharField(max_length=120)
    
    def __unicode__(self):
        return u"%d, %s" % (self.position, self.description)
    
    
class Assignment(models.Model):
    position = models.IntegerField()
    employee = models.ForeignKey(Employee)
    goal = models.ForeignKey(Goal)
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    

class AcceptanceCriteria(models.Model):
    goal = models.ForeignKey(Goal)
    STANDARD_CLASSIFICATION = (
                      ('O', 'Outstanding'),
                      ('E', 'Superior'),
                      ('S', 'Standard'),
                      ('NS', 'Needs Improvement'),
                      )
    standard = models.CharField(max_length=2,
                                choices=STANDARD_CLASSIFICATION)
    description = models.CharField(max_length=120, blank=True, null=True)
    expected_date = models.DateField()
    expected_percentage = models.IntegerField()
    
    def __unicode__(self):
        return u"%s para %s terminar el %d antes del  %s" % (self.goal, self.standard, self.expected_percentage, self.expected_date)
    
class Deliverable(models.Model):
    position = models.IntegerField()
    goal = models.ForeignKey(Goal)
    description = models.CharField(max_length=120)
    