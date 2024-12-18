import unittest
from class_variables import Student

class TestClassVariables(unittest.TestCase):

    def test_instance_variables(self):
        s1 = Student('kamal', 30)
        s2 = Student('kumar', 32)

        self.assertEqual(s1.name, 'kamal')
        self.assertEqual(s2.name, 'kumar')

        self.assertEqual(Student.class_year, 2024)
        self.assertEqual(Student.class_year, 2024)

    def test_class_variables(self):
        s1 = Student('Sponge Bob', 30)
        s2 = Student('Patrick', 35)

        self.assertEqual(Student.num_of_students, 2)

        s3 = Student('Sandy', 27)
        self.assertEqual(Student.num_of_students, 3)

        print(f"My graduating class of {Student.class_year} has {Student.num_of_students} students.")


if __name__ == "__main__":
    unittest.main()