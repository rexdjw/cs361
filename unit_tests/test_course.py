import unittest
from unit_tests.course import Course
from unit_tests.users import Users
from unit_tests.TA import TA


class TestCourse(unittest.TestCase):

    def setUp(self):
        self.course = Course(course_name="testCourse", department="testDepartment", course_number="100",instructor="testInstructor")

    def test_init_with_instructor(self):
        course = Course(course_name="testCourse", department="testDepartment", course_number="111",
                        instructor="testInstructor")
        self.assertTrue(course.courseName == "testCourse")
        self.assertTrue(course.department == "testDepartment")
        self.assertTrue(course.courseNumber == "111")
        self.assertTrue(course.instructor == "testInstructor")

    def test_init_without_instructor(self):
        course = Course(course_name="testCourse", department="testDepartment", course_number="111")
        self.assertTrue(course.courseName == "testCourse")
        self.assertTrue(course.department == "testDepartment")
        self.assertTrue(course.courseNumber == "111")
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
        pass

    def test_assign_TA_that_already_exists(self):
        pass

    def test_assign_TA_invalid_number_of_labs(self):
        pass

    def test_remove_TA(self):
        pass

    def test_remove_TA_that_does_not_exist(self):
        pass

    def test_display_assignments_one_assignment(self):
        pass

    def test_display_assignments_multiple_assignments(self):
        pass

    def test_create_lab_section(self):
        pass

    def test_create_lab_section_no_TA(self):
        pass
