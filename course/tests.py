from django.test import TestCase

from course.models import Course
from users.models import Users
from ta.models import TA


class TestCourse(TestCase):

    def setUp(self):
        self.testInstructor = Users.objects.create(username="testInstructor")
        self.course = Course.objects.create(courseName="testCourse", department="testDepartment", courseNumber="100",
                                            instructor=self.testInstructor)

        self.users = Users.objects.create(username="testUser")
        self.ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=1)

        self.courseWithTA = Course.objects.create(courseName="testCourseWithTA", department="testDepartment",
                                                  courseNumber="200", instructor=self.testInstructor)

        self.courseWithTA.assign_TA(ta=self.ta)

    def test_init_with_instructor(self):
        course = Course.objects.create(courseName="testCourse", department="testDepartment", courseNumber="100",
                             instructor=self.testInstructor)
        self.assertTrue(course.courseName == "testCourse")
        self.assertTrue(course.department == "testDepartment")
        self.assertTrue(course.courseNumber == "100")
        self.assertTrue(course.instructor == self.testInstructor)

    def test_init_without_instructor(self):
        course = Course.objects.create(courseName="testCourse", department="testDepartment", courseNumber="111")
        self.assertTrue(course.courseName == "testCourse")
        self.assertTrue(course.department == "testDepartment")
        self.assertTrue(course.courseNumber == "111")
        self.assertIsNone(course.instructor)

    def test_init_with_invalid_courseNumber(self):
        Course.objects.create(courseName="testCourse", department="testDepartment", courseNumber="111",
                      instructor=self.testInstructor)
        self.assertRaises(ValueError)

    def test_assign_instructor(self):
        courseWithoutInstructor = Course.objects.create(courseName="testCourse", department="testDepartment",
                                                        courseNumber="100")
        courseWithoutInstructor.assign_instructor(self.testInstructor)
        self.assertTrue(self.course.instructor == self.testInstructor)

    def test_remove_instructor(self):
        self.assertTrue(self.course.remove_instructor())
        self.assertIsNone(self.course.instructor)

    def test_assign_TA(self):
        ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=1)
        self.course.assign_TA(ta=ta)
        self.assertEqual(self.course.TAs.get(account=self.users), ta)
