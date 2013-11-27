from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_id = models.CharField(max_length=8)
    
    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_name,)

class Goal(models.Model):
    description = models.CharField(max_length=30)
    
    
class Assignment(models.Model):
    position = models.IntegerField()
    employee = models.ForeignKey(Employee)
    goal = models.ForeignKey(Goal)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    

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
    description = models.CharField(max_length=50)
    expected_date = models.DateField()
    expected_percentage = models.IntegerField(max_digits=5, decimal_places=2)
    
class Deliverable(models.Model):
    position = models.IntegerField()
    goal = models.ForeignKey(Goal)
    description = models.CharField(max_length=50)
    