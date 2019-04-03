import unittest
from unit_tests.course import Course
from unit_tests.users import Users
from unit_tests.TA import TA


class TestCourse(unittest.TestCase):

    def setUp(self):
        self.course = Course(course_name="testCourse", department="testDepartment", course_number="100",
                             instructor="testInstructor")

        self.users = Users("testUser", "12345")

        self.courseWithTA = Course(course_name="testCourseWithTA", department="testDepartment", course_number="200",
                             instructor="testInstructor")

        self.courseWithTA.assign_TA(ta=self.users, grader_status=False, number_of_labs=1)

    def test_init_with_instructor(self):
        course = Course(course_name="testCourse", department="testDepartment", course_number="111",
                        instructor="testInstructor")
        self.assertTrue(course.course_name == "testCourse")
        self.assertTrue(course.department == "testDepartment")
        self.assertTrue(course.course_number == "111")
        self.assertTrue(course.instructor == "testInstructor")

    def test_init_without_instructor(self):
        course = Course(course_name="testCourse", department="testDepartment", course_number="111")
        self.assertTrue(course.course_name == "testCourse")
        self.assertTrue(course.department == "testDepartment")
        self.assertTrue(course.course_number == "111")
        self.assertIsNone(course.instructor)

    def test_init_with_invalid_courseNumber(self):
        Course(course_name="testCourse", department="testDepartment", course_number="111", instructor="testInstructor")
        self.assertRaises(ValueError)

    def test_assign_instructor(self):
        self.course.assign_instructor("newInstructor")
        self.assertTrue(self.course.instructor == "newInstructor")

    def test_remove_instructor(self):
        self.assertTrue(self.course.remove_instructor())
        self.assertIsNone(self.course.instructor)

    def test_remove_instructor_with_no_instructor(self):
        course = Course(course_name="testCourse", department="testDepartment", course_number="111")
        self.assertFalse(course.remove_instructor())

    def test_assign_TA(self):
        self.course.assign_TA(ta=self.users, grader_status=False, number_of_labs=1)

        self.assertEqual(len(self.course.TAs.keys()), 1)
        ta = self.course.TAs.get(self.users.username)
        self.assertEqual(ta.ta.username, "testUser")

    def test_assign_TA_that_already_exists(self):
        self.course.assign_TA(ta=self.users, grader_status=False, number_of_labs=1)
        self.assertEqual(len(self.course.TAs.keys()), 1)

        with self.assertRaises(AssertionError) as context:
            self.course.assign_TA(ta=self.users, grader_status=False, number_of_labs=1)

            self.assertTrue('This TA already exists' in context.exception)

    def test_assign_TA_invalid_number_of_labs_number(self):
        with self.assertRaises(ValueError) as context:
            self.course.assign_TA(ta=self.users, grader_status=False, number_of_labs=-4)

            self.assertTrue('Number of labs is invalid' in context.exception)

    def test_assign_TA_invalid_number_of_labs_letters(self):
        with self.assertRaises(ValueError) as context:
            self.course.assign_TA(ta=self.users, grader_status=False, number_of_labs="c")

            self.assertTrue('Number of labs is invalid' in context.exception)

    def test_remove_TA(self):
        self.assertEqual(True, self.courseWithTA.remove_TA(self.users))
        self.assertEqual(len(self.courseWithTA.TAs.keys()), 0)

    def test_remove_TA_that_does_not_exist(self):
        self.assertEqual(False, self.course.remove_TA(self.users))

    def test_create_lab_section(self):
        self.courseWithTA.create_lab_section(lab_number=401, ta=self.courseWithTA.TAs.get(self.users))
        self.assertEqual(len(self.courseWithTA.labs.keys()), 1)

    def test_create_lab_section_no_TA(self):
        self.course.create_lab_section(lab_number=402)
        self.assertEqual(len(self.course.labs.keys()), 1)
