from django.db import models
from django.db.models.fields.files import FileField
from django.db.models.fields import FilePathField, CharField, DateTimeField
import os

# Create your models here.
class AssemblyInfo(models.Model):
    fullpath = FilePathField()
    title = CharField(max_length=120, blank = True, null = True)
    description = CharField(max_length=120, blank = True, null = True)
    version = CharField(max_length=120, blank = True, null = True)
    updated_on = DateTimeField(auto_now=True)
    project = CharField(max_length=120, blank = True, null = True)
    
    def __setattr__(self,key, value):
        super(AssemblyInfo, self).__setattr__(key, value) 
        if key == 'fullpath':
            print "*** %s:%s **" % (key, value) 
            f = value.split(os.sep)
            super(AssemblyInfo, self).__setattr__('project', 'pppppp' ) #f[len(f)-2:len(f)-1]
        