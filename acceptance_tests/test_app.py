
from unittest import TestCase, TestSuite, TextTestRunner, makeSuite
from main.models import YourClass
from django.test import TestCase

from main.models import YourClass
from users.models import Users
from course.models import Course
from ta.models import TA
from django.test import RequestFactory


class TestApp(TestCase):

    #def setUp(self):
        #self.app = App()
        #testSUser = Users("testSUName", "password", 8)
        #testSUser.create()
        #testTUser = Users("testTUName", "password", 1)
        #testTUser.create()
        #testCourse = Course("testCName", "testdept", 100)
        #testCourse.create()
        #testTA = TA(False, 0, testTUser)
        #testTA.create()

    def test_loginSuccess(self):
        # Users from any account (provided they have an account) logs in
        yourClass = YourClass()

        request = RequestFactory()


        self.users = Users.objects.create(username="admin", password="admin", roles=4)

        request.user = self.users

        print(request)

        #print(yourClass.command(s="login admin admin", request=self.users))
        result = yourClass.command(s="login admin admin", request=request)
        self.assertEqual(result, "Login successful.")

        #result = self.app.command("login Username password")
        #self.assertEqual(result, "Login successful.")

    def test_loginFailure(self):
        # Users from any account (provided they have an account) logs in with a wrong password
        result = self.app.command("login Username password")
        self.assertEqual(result, "Login failed, wrong password")

    # TODO - loginFAilure no such user

    # TODO - logout

    def test_createAccountSuccess(self):
        # Supervisor logged in, creating account with any role
        yourClass = YourClass()
        request = RequestFactory()

        users = Users.objects.create(username="admin", password="admin", roles=8)

        request.user = users
        result = yourClass.command(s="createAccount username password 2", request=request)
        self.assertEquals(result, "Account created successfully.")

    def test_createAccountFail(self):
        # Eligible Users creating duplicate Users
        users = Users.objects.create(username="admin", password="admin", roles=2)
        yourClass = YourClass()
        request = RequestFactory()
        request.user = users
        result = yourClass.command(s="createAccount new admin 2", request=request)
        #self.assertEquals(result, "Account created successfully.")
        #result = self.app.command("createAccount username password 1")
        self.assertEquals(result, "Permission denied - Your role may not create accounts!")

        # Administrator logged in, creating account of Administrator
        #result = self.app.command("createAccount username password 8")
        #self.assertEquals(result, "Permission denied - Cannot create account with that role!")

        # Ineglible Users logged in, creating account of any role
        #result = self.app.command("createAccount username password 1")
        #self.assertEquals(result, "Permission denied - Your role may not create accounts!")

    def test_deleteAccountSuccess(self):
        # Eligible Users logged in, deleting account with any role
        result = self.app.command("deleteAccount Username")
        self.assertEquals(result, "User deleted")

    def test_deleteAccountFail(self):
        # Eligible Users logged in, deleting nonexistent account
        result = self.app.command("deleteAccount Username")
        self.assertEquals(result, "No such user")

        # Administrator logged in, deleting administrator or supervisor account
        result = self.app.command("deleteAccount Username")
        self.assertEquals(result, "Permission denied - your role may not delete accounts of these type!")

        # Ineligible Users logged in, deleting account of any role
        result = self.app.command("deleteAccount Username")
        self.assertEquals(result, "Account Username deleted successfully.")

    def test_createCourseSuccess(self):
        # Eligible Users logged in, create course
        result = self.app.command("createCourse courseName department courseNumber")
        self.assertEquals(result, "Course created successfully.")

    def test_createCourseFail(self):
        # Eligible Users logged in, create duplicate course
        result = self.app.command("createCourse courseName department courseNumber")
        self.assertEquals(result, "Course courseName already exists!")

        # Ineigible Users logged in, create course
        result = self.app.command("createCourse courseName department courseNumber")
        self.assertEquals(result, "Permission Denied - Your role may not create courses!")

    def test_sendEmailSuccess(self):
        # Email is sent to the proper groups. No issues
        result = self.app.command("sendEmail ta subject content")
        self.assertEqual(result, "Successfully sent.")

    def test_sendEmailFailure(self):
        # Email failure is sent back to individual if they send an email to a group they should not be able to
        result = self.app.command("sendEmail unknowngroup subject content")
        self.assertEqual(result, "Group does not exist!")

    def test_assignInstructorSuccess(self):
        # Supervisors only - Successfully adds an instructor (that already exists) to a course
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Successfully added instructor to course")

    def test_assignInstructorPermissionDenied(self):
        # Users who is not a supervisor tries to add an instructor to a course
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Permission denied - your role may not add instructors to courses")

    def test_assignInvalidInstructorToCourse(self):
        # Supervisor only - tries to assign an instructor that doesn't exist to a course
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Account instructor does not exist")

    def test_assignInstructorToInvalidCourse(self):
        # Supervisors only - tries to add instructor to unassigned course.
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Course course does not exist")

    def test_removeInstructorSuccess(self):
        # Supervisors only - Successfully removes an instructor (that already exists) from a course
        result = self.app.command("removeInstructor instructor course")
        self.assertEqual(result, "Successfully removed instructor from course")

    def test_removeInstructorPermissionDenied(self):
        # Users who is not a supervisor tries to remove an instructor from a course
        result = self.app.command("removeInstructor instructor course")
        self.assertEqual(result, "Permission denied - your role may not remove instructors from courses")

    def test_removeInvalidInstructorFromCourse(self):
        # Supervisor only - tries to remove an instructor that doesn't exist from a course
        result = self.app.command("removeInstructor instructor course")
        self.assertEqual(result, "Account instructor does not exist")

    def test_removeInstructorFromInvalidCourse(self):
        # Supervisors only - tries to remove instructor from unassigned course.
        result = self.app.command("removeInstructor instructor course")
        self.assertEqual(result, "Course course does not exist")

    def test_assignTAToCourseSuccess(self):
        # Supervisors only - Successfully adds a TA to a course
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Successfully added TA to course")

    def test_assignTAToCoursePermissionDenied(self):
        # Users who is not a supervisor tries to add a TA to a course
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Permission denied - your role may not add TA's to courses")

    def test_assignInvalidTAToCourse(self):
        # Supervisor only - tries to add a TA that doesn't exist to a course
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Account TA does not exist")

    def test_assignTAToInvalidCourse(self):
        # Supervisor only - tries to add a TA to a course that doesn't exist
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Course course does not exist")

    def test_removeTAFromCourseSuccess(self):
        # Supervisors only - Successfully removes a TA from a course
        result = self.app.command("removeTACourse TA course")
        self.assertEqual(result, "Successfully removed TA from course")

    def test_removeTAFromCoursePermissionDenied(self):
        # Users who is not a supervisor tries to remove a TA from a course
        result = self.app.command("removeTACourse TA course")
        self.assertEqual(result, "Permission denied - your role may not remove TA's from courses")

    def test_removeInvalidTAFromCourse(self):
        # Supervisor only - tries to remove a TA that doesn't exist from a course
        result = self.app.command("removeTACourse TA course")
        self.assertEqual(result, "Account TA does not exist")

    def test_removeTAFromInvalidCourse(self):
        # Supervisor only - tries to remove a TA from a course that doesn't exist
        result = self.app.command("removeTACourse TA course")
        self.assertEqual(result, "Course course does not exist")

    def test_assignTAToLabSuccess(self):
        # Supervisor or Instructor - Successfully assigns a TA to a course
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Successfully added TA to lab")

    def test_assignTAToLabPermissionDenied(self):
        # Users tries to add TA to lab permission denied
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Permission denied - your role may not add TAs to lab sections")

    def test_assignInvalidTAToLab(self):
        # Supervisor only - tries to add a TA that doesn't exist to a course
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Account TA does not exist")

    def test_assignTAToInvalidLab(self):
        # Supervisor only - tries to add TA to a lab that doesn't exist
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Lab section lab does not exist")

    def test_removeTAFromLabSuccess(self):
        # Supervisor or Instructor - Successfully removes a TA from a course
        result = self.app.command("removeTALab TA lab")
        self.assertEqual(result, "Successfully removed TA from lab")

    def test_removeTAFromLabPermissionDenied(self):
        # Users tries to remove TA from lab permission denied
        result = self.app.command("removeTALab TA lab")
        self.assertEqual(result, "Permission denied - your role may not remove TAs from lab sections")

    def test_removeInvalidTAFromLab(self):
        # Supervisor only - tries to remove a TA that doesn't exist from a course
        result = self.app.command("removeTALab TA lab")
        self.assertEqual(result, "Account TA does not exist")

    def test_removeTAFromInvalidLab(self):
        # Supervisor only - tries to remove TA from a lab that doesn't exist
        result = self.app.command("removeTALab TA lab")
        self.assertEqual(result, "Lab section lab does not exist")

    def test_editContactInfoSuccess(self):
        # Users successfully edits a field in their contact info
        result = self.app.command("editContactInfo field revision")
        self.assertEqual(result, "field successfully revised")

    # TODO - editContactInfo while not logged in

    def test_editContactInfoFieldDoesNotExist(self):
        # Users failures to edit a field in their contact info because it doesn't exist
        result = self.app.command("editOwnContactInfo field revision")
        self.assertEqual(result, "Field field does not exist")

    def test_readTAAssignmentSuccess(self):
        # Users reads TA assignments
        result = self.app.command("readTAAssignment TA")
        self.assertEqual(result, "ta info info")

    def test_resdTAAssignmentFailure(self):
        # Users tries to look at a TA that doesn't exist
        result = self.app.command("readTAAssignment TA")
        self.assertEqual(result, "TA ta doesn't exist")

    def test_readAllTAAssignment(self):
        # Users reads all TA Assignments
        result = self.app.command("readAllTAAssignments")
        self.assertEqual(result, "TA info info")

    def test_readPublicContactInfoSuccess(self):
        # Users reads contact info for another Users
        result = self.app.command("readPublicContactInfo Users field")
        self.assertEqual(result, "Public info info")

    def test_readPublicContactInfoFailure(self):
        # Users unable to read contact info on invalid Users
        result = self.app.command("readPublicContactInfo Users field")
        self.assertEqual(result, "Users Users does not exist.")

    def test_editContactInfoSuccess(self):
        # Edit contact info for Users
        result = self.app.command("Users phonenumber email address officeHours")
        self.assertEqual(result, "Contact info set!")

    def test_editContactInfoFail(self):
        # Edit contact info for Users fail
        result = self.app.command("Users phonenumber email address officeHours")
        self.assertEqual(result, "Users does not exist!")

    def test_editAccountInfo(self):
        # Edit account info
        result = self.app.command("Usersname newUsersname password ta")
        self.assertEqual(result, "Users account info changed!")

    def test_editAccountInfoFail(self):
        # Edit account info
        result = self.app.command("Usersname newUsersname password ta")
        self.assertEqual(result, "Users does not exist!")

    def test_unkCommand(self):
        """unrecognized command"""
        cmd = "skjkdhjfhjskhk"
        result = self.app.command(cmd)
        self.assertEqual(result, "Unrecognized command: " + cmd)