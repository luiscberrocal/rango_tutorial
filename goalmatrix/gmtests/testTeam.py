from django.test import TestCase
from goalmatrix.models import Team
from django.db.utils import IntegrityError

# Create your tests here.
class EmployeeTest(TestCase):
    fixtures = ['goalmatrix_fixtures.json',]
    def setUp(self):
        self.team = Team.objects.create(name="Team long", short_name ="LONG")

    def test_fixture_load(self):
        count = Team.objects.count()
        self.assertEqual(count, 2)
    
    def test_models(self):
        self.assertEqual(self.team.short_name, "LONG")
        
    def test_cannot_create_duplicate_short_name(self):
        try:
            Team.objects.create(name="Team long", short_name ="LONG")
        except IntegrityError as e:
            self.assertEqual(e.args[0], 'column short_name is not unique')
            return
        self.fail("Was able to add duplicate short_name")
        
        

        