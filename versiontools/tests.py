from django.test import TestCase
from versiontools.models import AssemblyInfo
from django.utils.timesince import timesince
from django.utils.datetime_safe import datetime

# Create your tests here.
class AssembyInfoTest(TestCase):
    
    def test_create(self):
        data = {'fullpath'     : r'C:\Users\lberrocal\Documents\Visual Studio 2010\Projects\vessel_scheling_app\5-VesselScheduleEngine\VsApplicationData\My Project\AssemblyInfo.vb ',
                'title'        : 'Vessel Schedule WorkBench',
                'description'  : '',
                'version'      : '1.2.6'}
        ai = AssemblyInfo.objects.create(**data)
        self.assertEqual(ai.fullpath, data['fullpath'])
        self.assertEqual(ai.title, data['title'])
        self.assertEqual(ai.description, data['description'])
        self.assertEqual(ai.version, data['version'])
        print ai.updated_on
        print datetime.now()
        print ai.project
        