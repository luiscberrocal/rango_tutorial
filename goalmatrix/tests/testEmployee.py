from django.test import TestCase
from goalmatrix.models import Employee, Team

# Create your tests here.
class EmployeeTest(TestCase):
    fixtures = ['goalmatrix_fixtures.json',]
    def setUp(self):
        team = Team.objects.create(name="Team long", short_name ="LONG")
        self.employee = Employee.objects.create(first_name="James", last_name="Bond",
                                                username="jbond", company_id = "1795897",
                                                team = team)
    def test_fixture_load(self):
        count = Employee.objects.count()
        self.assertEqual(count, 5)
    
    def test_models(self):
        self.assertEqual(self.employee.username, "jbond")
        
    def test_get_employee(self):
        emp = Employee.objects.get(username="jbond")
        self.assertEqual(emp.username, "jbond")
        
    def test_get_fixture_employee(self):
        emp = Employee.objects.get(username="jdominguez")
        self.assertEqual(emp.username, "jdominguez")
        self.assertEqual(emp.first_name, "Joe")
        