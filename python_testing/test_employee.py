import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # setUpClass is like beforeAll function
        # which executes once before for whole tests in file
        
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        # tearDownClass is like afterAll fuction
        # which executes once after for whole tests in file
        print("tearDownClass")

    def setUp(self):
        # this will execute befor each test
        print('setUp')
        self.emp_1 = Employee('Kamal', 'Jeldi', 50000)
        self.emp_2 = Employee('Kumar', 'Jeldi', 60000)
    
    def tearDown(self):
        print("tearDown")
        pass

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, 'Kamal.Jeldi@email.com')
        self.assertEqual(self.emp_2.email, 'Kumar.Jeldi@email.com')

        self.emp_1.first = 'kamal'
        self.emp_1.last = 'jeldi'

        self.emp_2.first = 'kumar'
        self.emp_2.last = 'jeldi'

        self.assertEqual(self.emp_1.email, 'kamal.jeldi@email.com')
        self.assertEqual(self.emp_2.email, 'kumar.jeldi@email.com')
    
    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.full_name, 'Kamal Jeldi')
        self.assertEqual(self.emp_2.full_name, 'Kumar Jeldi')

        self.emp_1.first = 'kamal'
        self.emp_1.last = 'jeldi'

        self.emp_2.first = 'kumar'
        self.emp_2.last = 'jeldi'

        self.assertEqual(self.emp_1.full_name, 'kamal jeldi')
        self.assertEqual(self.emp_2.full_name, 'kumar jeldi')


if __name__ == "__main__":
    unittest.main()