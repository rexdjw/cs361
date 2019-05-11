
from unittest import TestCase, TestSuite, TextTestRunner, makeSuite
from main.models import YourClass
from django.test import TestCase

from main.models import YourClass
from users.models import Users
from course.models import Course
from ta.models import TA
from django.test import RequestFactory


class TestApp(TestCase):

    def setUp(self):
        self.app = YourClass()
        self.request = RequestFactory().get('/')
        from django.contrib.sessions.middleware import SessionMiddleware
        self.middleware = SessionMiddleware()
        self.middleware.process_request(self.request)

        self.request.session.save()

    def test_loginSuccess(self):

        self.users = Users.create(username="admin", password="admin", roles=4)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users


        result = self.app.command(s="login admin admin", request=self.request)
        self.assertEqual(result, "Login successful.")


    def test_loginFailure(self):
        # Users from any account (provided they have an account) logs in with a wrong password
        self.users = Users.create(username="test123", password="admin", roles=4)
        self.users.set_password('carl')
        self.users.save()

        self.request.user = self.users
        result = self.app.command("login test123 admin", request=self.request)
        self.assertEqual(result, "Login failed, wrong password")


    def test_loginFailureNoUser(self):
        # Users from any account (provided they have an account) logs in with a wrong password

        result = self.app.command("login test123 admin", request=self.request)
        self.assertEqual(result, "Login failed, no such user")

    def test_logout(self):
        self.users = Users.create(username="admin", password="admin", roles=4)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login admin admin", request=self.request)
        result = self.app.command("logout", request=self.request)
        self.assertEqual(result, "Logged out")

    def test_createAccountSuccess(self):
        self.users = Users.create(username="admin", password="admin", roles=8)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login admin admin", request=self.request)

        result = self.app.command(s="createAccount username password 2", request=self.request)
        self.assertEquals(result, "Account created successfully.")

    def test_createAccountFailDup(self):
        # Eligible Users creating duplicate Users
        self.users = Users.create(username="admin", password="admin", roles=8)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login admin admin", request=self.request)
        self.app.command(s="createAccount username password 2", request=self.request)

        result = self.app.command(s="createAccount username password 2", request=self.request)
        self.assertEquals(result, "Account already exists!")

    def test_createAccountFailPermission(self):
        self.users = Users.create(username="admin", password="admin", roles=6)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login admin admin", request=self.request)
        result = self.app.command(s="createAccount username password 8", request=self.request)
        self.assertEquals(result, "Permission denied - Your role may not create accounts of this type!")

    def test_createAccountFailAccount(self):
        self.users = Users.create(username="admin", password="admin", roles=0)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login admin admin", request=self.request)
        result = self.app.command(s="createAccount username password 8", request=self.request)
        self.assertEquals(result, "Permission denied - Your role may not create accounts!")

    def test_deleteAccountSuccess(self):
        self.users = Users.create(username="admin", password="admin", roles=8)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login admin admin", request=self.request)

        result = self.app.command("deleteAccount admin", request=self.request)
        self.assertEquals(result, "User deleted")

    def test_deleteAccountFail(self):
        # Eligible Users logged in, deleting nonexistent account
        self.users = Users.create(username="admin", password="admin", roles=8)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login admin admin", request=self.request)

        result = self.app.command("deleteAccount Username", request=self.request)
        self.assertEquals(result, "No such user")


    def test_deleteFailPermission(self):
        self.users = Users.create(username="admin", password="admin", roles=8)
        self.users.set_password('admin')
        self.users.save()

        self.users = Users.create(username="check", password="check", roles=6)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login check check", request=self.request)
        result = self.app.command("deleteAccount admin", request=self.request)
        self.assertEquals(result, "Permission denied - Your role may not delete accounts of this type!")

    def test_deleteFail_IneligbleUser(self):
        self.users = Users.create(username="admin", password="admin", roles=8)
        self.users.set_password('admin')
        self.users.save()

        self.users = Users.create(username="check", password="check", roles=1)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login check check", request=self.request)
        result = self.app.command("deleteAccount admin", request=self.request)
        self.assertEquals(result, "Permission denied - Your role may not delete accounts of this type!")


    def test_createCourseSuccess(self):
        # Eligible Users logged in, create course
        result = self.app.command("createCourse courseName department courseNumber", request=self.request)
        self.assertEquals(result, "Pass - implemented in Web Interface not Command Line.")

    def test_createCourseFail(self):
        # Eligible Users logged in, create duplicate course
        result = self.app.command("createCourse courseName department 5",request=self.request)
        self.assertEquals(result, "Pass - implemented in Web Interface not Command Line.")

        # Ineigible Users logged in, create course
        result = self.app.command("createCourse courseName department 5", request=self.request)
        self.assertEquals(result, "Pass - implemented in Web Interface not Command Line.")

    def test_sendEmailSuccess(self):
        # Email is sent to the proper groups. No issues
        result = self.app.command("sendEmail ta subject content", request=self.request)
        self.assertEqual(result, "Email sent successfully.")

    def test_sendEmailFailure(self):
        # Email failure is sent back to individual if they send an email to a group they should not be able to
        result = self.app.command("sendEmail unknowngroup subject content", request=self.request)
        self.assertEqual(result, "Failed - permission denied.")

    def test_assignInstructorSuccess(self):
        # Supervisors only - Successfully adds an instructor (that already exists) to a course
        result = self.app.command("assignInstructor instructor course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignInstructorPermissionDenied(self):
        # Users who is not a supervisor tries to add an instructor to a course
        result = self.app.command("assignInstructor instructor course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignInvalidInstructorToCourse(self):
        # Supervisor only - tries to assign an instructor that doesn't exist to a course
        result = self.app.command("assignInstructor instructor course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignInstructorToInvalidCourse(self):
        # Supervisors only - tries to add instructor to unassigned course.
        result = self.app.command("assignInstructor instructor course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeInstructorSuccess(self):
        # Supervisors only - Successfully removes an instructor (that already exists) from a course
        result = self.app.command("removeInstructor instructor course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeInstructorPermissionDenied(self):
        # Users who is not a supervisor tries to remove an instructor from a course
        result = self.app.command("removeInstructor instructor course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeInvalidInstructorFromCourse(self):
        # Supervisor only - tries to remove an instructor that doesn't exist from a course
        result = self.app.command("removeInstructor instructor course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeInstructorFromInvalidCourse(self):
        # Supervisors only - tries to remove instructor from unassigned course.
        result = self.app.command("removeInstructor instructor course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignTAToCourseSuccess(self):
        # Supervisors only - Successfully adds a TA to a course
        result = self.app.command("assignTACourse TA course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignTAToCoursePermissionDenied(self):
        # Users who is not a supervisor tries to add a TA to a course
        result = self.app.command("assignTACourse TA course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignInvalidTAToCourse(self):
        # Supervisor only - tries to add a TA that doesn't exist to a course
        result = self.app.command("assignTACourse TA course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignTAToInvalidCourse(self):
        # Supervisor only - tries to add a TA to a course that doesn't exist
        result = self.app.command("assignTACourse TA course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeTAFromCourseSuccess(self):
        # Supervisors only - Successfully removes a TA from a course
        result = self.app.command("removeTACourse TA course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeTAFromCoursePermissionDenied(self):
        # Users who is not a supervisor tries to remove a TA from a course
        result = self.app.command("removeTACourse TA course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeInvalidTAFromCourse(self):
        # Supervisor only - tries to remove a TA that doesn't exist from a course
        result = self.app.command("removeTACourse TA course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeTAFromInvalidCourse(self):
        # Supervisor only - tries to remove a TA from a course that doesn't exist
        result = self.app.command("removeTACourse TA course", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignTAToLabSuccess(self):
        # Supervisor or Instructor - Successfully assigns a TA to a course
        result = self.app.command("assignTALab TA lab", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignTAToLabPermissionDenied(self):
        # Users tries to add TA to lab permission denied
        result = self.app.command("assignTALab TA lab", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignInvalidTAToLab(self):
        # Supervisor only - tries to add a TA that doesn't exist to a course
        result = self.app.command("assignTALab TA lab", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_assignTAToInvalidLab(self):
        # Supervisor only - tries to add TA to a lab that doesn't exist
        result = self.app.command("assignTALab TA lab", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeTAFromLabSuccess(self):
        # Supervisor or Instructor - Successfully removes a TA from a course
        result = self.app.command("removeTALab TA lab", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeTAFromLabPermissionDenied(self):
        # Users tries to remove TA from lab permission denied
        result = self.app.command("removeTALab TA lab", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeInvalidTAFromLab(self):
        # Supervisor only - tries to remove a TA that doesn't exist from a course
        result = self.app.command("removeTALab TA lab", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_removeTAFromInvalidLab(self):
        # Supervisor only - tries to remove TA from a lab that doesn't exist
        result = self.app.command("removeTALab TA lab", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_editContactInfoSuccess(self):
        # Users successfully edits a field in their contact info
        self.users = Users.create(username="admin", password="admin", roles=8)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login admin admin", request=self.request)

        result = self.app.command("editContactInfo 1 2 3 4 5 6", request=self.request)
        self.assertEqual(result, "field successfully revised")

    def test_editContactInfoFail(self):
        result = self.app.command("editContactInfo 1 2 3 4 5 6", request=self.request)
        self.assertEqual(result, "Login a user first")

    def test_editContactInfoFieldDoesNotExist(self):
        # Users failures to edit a field in their contact info because it doesn't exist
        self.users = Users.create(username="admin", password="admin", roles=8)
        self.users.set_password('admin')
        self.users.save()

        self.request.user = self.users

        self.app.command(s="login admin admin", request=self.request)

        result = self.app.command("editContactInfo 1 2 3 4 5 6 7", request=self.request)
        self.assertEqual(result, "Field does not exist")

    def test_readTAAssignmentSuccess(self):
        # Users reads TA assignments
        result = self.app.command("readTAAssignment TA", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_readTAAssignmentFailure(self):
        # Users tries to look at a TA that doesn't exist
        result = self.app.command("readTAAssignment TA", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_readAllTAAssignment(self):
        # Users reads all TA Assignments
        result = self.app.command("readAllTAAssignments", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_readPublicContactInfoSuccess(self):
        # Users reads contact info for another Users
        result = self.app.command("readPublicContactInfo Users field", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_readPublicContactInfoFailure(self):
        # Users unable to read contact info on invalid Users
        result = self.app.command("readPublicContactInfo Users field", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")


    def test_editAccountInfo(self):
        # Edit account info
        result = self.app.command("editAccount newUsersname password ta", request=self.request)
        self.assertEqual(result, "Pass - implemented in Web Interface not Command Line.")

    def test_unkCommand(self):
        """unrecognized command"""
        cmd = "skjkdhjfhjskhk"
        result = self.app.command(cmd, request=self.request)
        self.assertEqual(result, "Unrecognized command: " + cmd)