from random import randint

from django.test import TestCase

from course.models import Course
from users.models import Users
from ta.models import TA
from contactinfo.models import ContactInfo
from lab.models import Lab



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

    def test_remove_TA(self):
        ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=1)
        self.course.assign_TA(ta=ta)


    def test_create_lab_section(self):
        x = 801

        self.course.create_lab_section(x)


class TestContactInfo(TestCase):
    def setUp(self):
        users = Users.objects.create(username="testUser")

        self.ci = ContactInfo.objects.create(account=users, name="myName", phoneNumber="4145551234",
                                        email="foo@uwm.edu", address="1234 Street St, Milwaukee, WI, 53211")

    def testInit(self):
        self.assertEqual("myName", self.ci.name)
        self.assertEqual("4145551234", self.ci.phoneNumber)
        self.assertEqual("foo@uwm.edu", self.ci.email)
        self.assertEqual("1234 Street St, Milwaukee, WI, 53211", self.ci.address)
        self.assertEqual("", self.ci.officeHours)
        self.assertEqual("", self.ci.officeNumber)

    def testGetPublic(self):
        infolist = self.ci.get_public()
        self.assertEqual(infolist, ["myName", "foo@uwm.edu", "", ""])

    def testGetPrivate(self):
        infolist = self.ci.get_private()
        self.assertEqual(infolist, ["myName", "4145551234", "foo@uwm.edu", "1234 Street St, Milwaukee, WI, 53211", "", ""])

    def testUpdateName(self):
        self.assertTrue(self.ci.name == "myName")
        self.ci.updateName("newName")
        self.assertTrue(self.ci.name == "newName")

    def testUpdateEmail(self):
        self.assertTrue(self.ci.email == "foo@uwm.edu")
        self.ci.updateEmail("newEmail@uwm.edu")
        self.assertTrue(self.ci.email == "newEmail@uwm.edu")

    def testUpdateOfficeHours(self):
        self.assertTrue(self.ci.officeHours == "")
        self.ci.updateOfficeHours("10am")
        self.assertTrue(self.ci.officeHours == "10am")

    def testUpdateOfficeNumber(self):
        self.assertTrue(self.ci.officeHours == "")
        self.ci.updateOfficeNumber("123 EMS")
        self.assertTrue(self.ci.officeNumber == "123 EMS")

    def testUpdatePhoneNumber(self):
        self.assertTrue(self.ci.phoneNumber == "4145551234")
        self.ci.updatePhoneNumber("4142223333")
        self.assertTrue(self.ci.phoneNumber == "4142223333")

    def testUpdateAddress(self):
        self.assertTrue(self.ci.address == "1234 Street St, Milwaukee, WI, 53211")
        self.ci.updateAddress("555 Ave, Milwaukee, WI, 53211")
        self.assertTrue(self.ci.address == "555 Ave, Milwaukee, WI, 53211")

class TestLab(TestCase):

    def setUp(self):
        self.users = Users.objects.create(username="testUser")
        self.ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=1)


    def test_constructor_2(self):
        lab = Lab.objects.create(labNumber=400)
        self.assertEqual(lab.labNumber, 400)

    def test_constructor_3(self):
        with self.assertRaises(ValueError):
            Lab.objects.create(labNumber="hello")

    def test_assign_TA_1(self):
        lab = Lab.objects.create(labNumber=401)
        lab.assign_TA(self.ta)
        self.assertEqual(lab.TAs.get(account=self.users), self.ta)

    def test_assign_TA_2(self):
        lab = Lab.objects.create(labNumber=401)
        ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=0)
        lab.assign_TA(ta)
        self.assertEqual(lab.TAs.get(account=self.users), ta)

    def test_assign_TA_3(self):
        lab = Lab.objects.create(labNumber=401)
        ta = TA.objects.create(account=self.users, graderStatus=True, numberOfLabs=10)
        lab.assign_TA(ta)
        self.assertEqual(lab.TAs.get(account=self.users), ta)

class TestTA(TestCase):

    def setUp(self):
        self.users = Users.objects.create(username="testUser")
        self.ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=1)

    def test_constructor_1(self):
        tc1 = TA.objects.create(account=self.users, graderStatus=True, numberOfLabs=4)
        self.assertEqual(tc1.graderStatus, True)
        self.assertEqual(tc1.numberOfLabs, 4)

    def test_constructor_2(self):
        tc2 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=9)
        self.assertEqual(tc2.graderStatus, False)
        self.assertEqual(tc2.numberOfLabs, 9)

    def test_constructor_3(self):
        tc3 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=9.4)
        self.assertEqual(tc3.graderStatus, False)
        self.assertEqual(tc3.numberOfLabs, 9.4)

    def test_constructor_4(self):
        tc4 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=4)
        self.assertEqual(tc4.graderStatus, False)
        self.assertEqual(tc4.numberOfLabs, 4)

    def test_constructor_5(self):
        tc5 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=-4)
        self.assertEqual(tc5.graderStatus, False)
        self.assertEqual(tc5.numberOfLabs, -4)

    def test_constructor_6(self):
        tc6 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=0)
        self.assertEqual(tc6.graderStatus, False)
        self.assertEqual(tc6.numberOfLabs, 0)

    # Test setTAStatus
    def test_setTAStatus_1(self):
        self.ta.set_ta_status(grader_status=False, number_of_labs=0)
        self.assertEqual(self.ta.graderStatus, False)
        self.assertTrue(self.ta.number_of_labs == 0)

    def test_setTAStatus_2(self):
        self.ta.set_ta_status(grader_status=True, number_of_labs=0)
        self.assertFalse(self.ta.grader_status is False)
        self.assertTrue(self.ta.number_of_labs == 0)

    def test_setTAStatus_3(self):
        self.assertRaises(ValueError, self.ta.set_ta_status(grader_status=True, number_of_labs=-5))

    def test_setTAStatus_4(self):
        self.assertRaises(ValueError, self.ta.set_ta_status(grader_status=True, number_of_labs=0.4))

    def test_setTAStatus_5(self):
        self.assertRaises(ValueError, self.ta.set_ta_status(grader_status="Hello", number_of_labs=0))

    def test_setTAStatus_6(self):
        self.assertRaises(ValueError, self.ta.set_ta_status(grader_status='G', number_of_labs=4))

    def test_setTAStatus_7(self):
        self.assertRaises(ValueError, self.ta.set_ta_status(grader_status=9, number_of_labs=2))

    def test_setTAStatus_8(self):
        self.assertRaises(ValueError, self.ta.set_ta_status(grader_status=True, number_of_labs='r'))

    def test_setTAStatus_9(self):
        self.assertRaises(ValueError, self.ta.set_ta_status(grader_status=False, number_of_labs="Hi"))

    def test_setTAStatus_10(self):
        self.assertRaises(ValueError, self.ta.set_ta_status(grader_status=False, number_of_labs=False))


class TestUser(TestCase):

    def setUp(self):
        self.user = Users()

    def tearDown(self):
        self.user = None

    def test_create_account(self):

        Users.create("jayson", "12345", 8).save()
        self.user = Users.objects.get(username="jayson")

        self.assertTrue(self.user.username == "jayson")
        self.assertFalse(self.user.username == "12345")

    def test_is_super0(self):

        Users.create("Sean", "1234", randint(0, 15) | 8).save()
        self.user = Users.objects.get(username="Sean")
        self.assertTrue(self.user.is_super())

    def test_is_super1(self):

        Users.create("Sean", "1234", randint(0, 15) & 7).save()
        self.user = Users.objects.get(username="Sean")
        self.assertFalse(self.user.is_super())

    def test_is_admin0(self):

        Users.create("Sean", "1234", randint(0, 15) | 4).save()
        self.user = Users.objects.get(username="Sean")
        self.assertTrue(self.user.is_admin())

    def test_is_admin1(self):

        Users.create("Sean", "1234", randint(0, 15) & 11).save()
        self.user = Users.objects.get(username="Sean")
        self.assertFalse(self.user.is_admin())

    def test_is_instructor0(self):

        Users.create("Sean", "1234", randint(0, 15) | 2).save()
        self.user = Users.objects.get(username="Sean")
        self.assertTrue(self.user.is_instructor())

    def test_is_instructor1(self):

        Users.create("Sean", "1234", randint(0, 15) & 13).save()
        self.user = Users.objects.get(username="Sean")
        self.assertFalse(self.user.is_instructor())

    def test_is_ta0(self):

        Users.create("Sean", "1234", randint(0, 15) | 1).save()
        self.user = Users.objects.get(username="Sean")
        self.assertTrue(self.user.is_ta())

    def test_is_ta1(self):

        Users.create("Sean", "1234", randint(0, 15) & 14).save()
        self.user = Users.objects.get(username="Sean")
        self.assertFalse(self.user.is_ta())

    def test_edit_account_info0(self):

        Users.create("rock", "Ilikeprogramming", 0).save()
        self.user = Users.objects.get(username="rock")

        self.user.reset_username("jrock")

        self.assertEqual(self.user.username, "jrock")

    def test_edit_account_info1(self):
        Users.create("rock", "Ilikeprogramming", 0).save()
        self.user = Users.objects.get(username="rock")

        self.user.reset_password("Ilove361")

        self.assertEqual(self.user.password, "Ilove361")

    def test_edit_account_info2(self):

        Users.create("rock", "Ilikeprogramming", 0).save()
        self.user = Users.objects.get(username="rock")

        self.user.reset_roles(2)

        self.assertEqual(self.user.roles, 2)

    def test_edit_account_info3(self):

        Users.create("rock", "Ilikeprogramming", 0).save()
        self.user = Users.objects.get(username="rock")

        self.user.reset_username("jrock")
        self.user.reset_password("Ilove361")
        self.user.reset_roles(2)

        self.assertEqual(self.user.username, "jrock")
        self.assertEqual(self.user.password, "Ilove361")
        self.assertEqual(self.user.roles, 2)

    def test_is_above0(self):
        Users.create("name", "pass", 0).save()
        self.user = Users.objects.get(username="name")

        self.assertEqual(self.user.is_above(0), False)

    def test_is_above1(self):
        Users.create("name", "pass", 1).save()
        self.user = Users.objects.get(username="name")

        self.assertEqual(self.user.is_above(0), True)

    def test_is_above2(self):
        Users.create("name", "pass", 4).save()
        self.user = Users.objects.get(username="name")

        self.assertEqual(self.user.is_above(4), False)

    def test_is_above3(self):
        Users.create("name", "pass", 4).save()
        self.user = Users.objects.get(username="name")

        self.assertEqual(self.user.is_above(2), True)

    def test_is_at_least0(self):
        Users.create("name", "pass", 0).save()
        self.user = Users.objects.get(username="name")

        self.assertEqual(self.user.is_at_least(1), False)

    def test_is_at_least1(self):
        Users.create("name", "pass", 1).save()
        self.user = Users.objects.get(username="name")

        self.assertEqual(self.user.is_at_least(1), True)

    def test_is_at_least2(self):
        Users.create("name", "pass", 3).save()
        self.user = Users.objects.get(username="name")

        self.assertEqual(self.user.is_at_least(4), False)

    def test_is_at_least3(self):
        Users.create("name", "pass", 4).save()
        self.user = Users.objects.get(username="name")

        self.assertEqual(self.user.is_at_least(4), True)


    def test_set_contact_info0(self):

        Users.create("username", "password", 0).save()
        self.user = Users.objects.get(username="username")

        name = "myName"
        ph_num = "4145551234"
        email = "foo@uwm.edu"
        address = "1234 Street St, Milwaukee, WI, 53211"
        o_hours = ""
        o_num = ""

        self.user.set_contact_info(name, ph_num, email, address, o_hours, o_num)

        self.assertEqual(self.user.contactinfo.name, name)
        self.assertEqual(self.user.contactinfo.phoneNumber, ph_num)
        self.assertEqual(self.user.contactinfo.email, email)
        self.assertEqual(self.user.contactinfo.address, address)
        self.assertEqual(self.user.contactinfo.officeHours, o_hours)
        self.assertEqual(self.user.contactinfo.officeNumber, o_num)

    def test_set_contact_info1(self):

        Users.create("username", "password", 0).save()
        self.user = Users.objects.get(username="username")

        name = "myName"
        ph_num = "4145551234"
        email = "foo@uwm.edu"
        address = "1234 Street St, Milwaukee, WI, 53211"

        self.user.set_contact_info(name, ph_num, email, address)

        self.assertEqual(self.user.contactinfo.name, name)
        self.assertEqual(self.user.contactinfo.phoneNumber, ph_num)
        self.assertEqual(self.user.contactinfo.email, email)
        self.assertEqual(self.user.contactinfo.address, address)

    def test_to_string0(self):

        Users.create("username", "password", 0).save()
        self.user = Users.objects.get(username="username")

        self.assertEqual(str(self.user), "User username has no role permissions.")

    def test_to_string1(self):
        Users.create("username", "password", 1).save()
        self.user = Users.objects.get(username="username")

        self.assertEqual(str(self.user), "User username has [TA] role permissions.")

    def test_to_string2(self):
        Users.create("username", "password", 10).save()
        self.user = Users.objects.get(username="username")

        self.assertEqual(str(self.user), "User username has [Supervisor] [Instructor] role permissions.")

    def test_print_admin0(self):

        Users.create("username", "password", randint(0, 15) & 3).save()
        self.user = Users.objects.get(username="username")

        self.assertEqual(self.user.printAdmin(), "[Non-admin]")

    def test_print_admin1(self):
        Users.create("username", "password", randint(0, 15) & 7 | 4).save()
        self.user = Users.objects.get(username="username")

        self.assertEqual(self.user.printAdmin(), "[Administrator]")

    def test_print_admin2(self):
        Users.create("username", "password", randint(0, 15) | 8).save()
        self.user = Users.objects.get(username="username")

        self.assertEqual(self.user.printAdmin(), "[Supervisor]")