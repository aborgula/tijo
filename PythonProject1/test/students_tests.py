import unittest
from src.students import StudentManagement

class TestStudentManagement(unittest.TestCase):

    def test_add_student(self):

        #given
        student_management = StudentManagement()
        expected = True

        #when
        result = student_management.add_student(321,"Jola", 17)

        #then
        self.assertEqual(expected, result)

    def test_add_student_id_none(self):

        #given
        student_management = StudentManagement()
        expected = False

        #when
        result = student_management.add_student(None,"Jola", 18)

        #then
        self.assertEqual(expected, result)

    def test_update_students(self):

        #given
        student_management = StudentManagement()
        expected = True

        #when
        result = student_management.update_student()




if __name__ == '__main__':
    unittest.main()