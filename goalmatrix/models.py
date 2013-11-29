from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Team(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10, unique=True)
    
    def __unicode__(self):
        return u"%s, %s" % (self.short_name, self.name,)

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    company_id = models.CharField(max_length=8, 
                                  validators=[RegexValidator(
                                            regex='^\d{7}$', message='company id must be 7 digits', 
                                            code='invalid_company_id'),],
                                  unique=True)
    team = models.ForeignKey(Team, null=True, blank=True)
    
    def total_assignment(self):
        ta = 0
        for assign in self.assignment_set.all():
            ta += assign.weight
            #print "ddddddddddddddddd %d" % (ta)
        return ta

    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_name,)

class Goal(models.Model):
    position = models.IntegerField()
    description = models.CharField(max_length=120)
    
    def has_all_acceptance_criteria(self):
        return self.acceptancecriteria_set.count() == 4
    
    class Meta:
        ordering = ['position']
    
    def __unicode__(self):
        return u"%d, %s" % (self.position, self.description)
    
    
class Assignment(models.Model):
    position = models.IntegerField()
    employee = models.ForeignKey(Employee)
    goal = models.ForeignKey(Goal)
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    class Meta:
        ordering = ['position']
        
class StandardClassification(models.Model):
    class Meta:
        ordering = ['-grade']
    STANDARD_CLASSIFICATION = (
                      ('O', 'Outstanding'),
                      ('E', 'Superior'),
                      ('S', 'Satisfactory'),
                      ('N', 'Needs Improvement'),
                      )
    letter = models.CharField(max_length=1,
                              choices=STANDARD_CLASSIFICATION,
                              primary_key=True)
    grade = models.DecimalField(decimal_places=2, max_digits=5)
    
    def __unicode__(self):
        return u'%s %d' % (self.letter, self.grade)
    
class AcceptanceCriteria(models.Model):
    goal = models.ForeignKey(Goal)
    
    DATE_DEFINITION_CHOICES =(('BEFORE', 'Before'), ('AFTER', 'After'), ('NA', 'Not Applicable'))
    standard = models.ForeignKey(StandardClassification)
    description = models.CharField(max_length=120, blank=True, null=True)
    date_definition = models.CharField(max_length=8, 
                                       choices = DATE_DEFINITION_CHOICES,
                                       default= DATE_DEFINITION_CHOICES[0][0])
    expected_date = models.DateField()
    expected_percentage = models.IntegerField(default=100)
    
    def __unicode__(self):
        if self.date_definition == 'BEFORE':
            return u"Terminar el %.0f%% antes del %s. (%s)" % (self.expected_percentage, self.expected_date.strftime('%d-%b-%Y'), self.standard,)
        elif self.date_definition == 'AFTER':
            return u"Terminar el %.0f%% despues del %s. (%s)" % (self.expected_percentage, self.expected_date.strftime('%d-%b-%Y'), self.standard,)
        else:
            return u"%s para %s avance %d fecha  %s" % (self.goal, self.standard, self.expected_percentage, self.expected_date)
    
class Deliverable(models.Model):
    position = models.IntegerField()
    goal = models.ForeignKey(Goal)
    description = models.CharField(max_length=120)
    