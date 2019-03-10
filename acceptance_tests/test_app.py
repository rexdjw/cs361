from unittest import TestCase, TestSuite, TextTestRunner, makeSuite
from app import App


class TestApp(TestCase):

    def setUp(self):
        self.app = App()

    def test_loginSuccess(self):
        # User from any account (provided they have an account) logs in
        result = self.app.command("login username password")
        self.assertEqual(result, "Login successful.")

    def test_loginFailure(self):
        # User from any account (provided they have an account) logs in with a wrong password or username
        result = self.app.command("login username password")
        self.assertEqual(result, "Invalid password or username.")

    def test_createAccountSuccess(self):
        # Supervisor logged in, creating account with any role
        result = self.app.command("createAccount username password role")
        self.assertEquals(result, "Account {username} created successfully.")

        # Administrator logged in, creating account of Instructor or TA
        result = self.app.command("createAccount username password role")
        self.assertEquals(result, "Account {username} created successfully.")

    def test_createAccountFail(self):
        # Eligible user creating duplicate user
        result = self.app.command("createAccount username password role")
        self.assertEquals(result, "Account {username} already exists!")

        # Administrator logged in, creating account of Administrator
        result = self.app.command("createAccount username password role")
        self.assertEquals(result, "Permission denied - Cannot create account with that role!")

        # Ineglible user logged in, creating account of any role
        result = self.app.command("createAccount username password role")
        self.assertEquals(result, "Permission denied - Your role may not create accounts!")

    def test_deleteAccountSuccess(self):
        # Supervisor logged in, deleting account with any role
        result = self.app.command("deleteAccount username")
        self.assertEquals(result, "Account {username} deleted successfully.")

        # Administrator logged in, deleting account of Instructor or TA
        result = self.app.command("createAccount username")
        self.assertEquals(result, "Account {username} deleted successfully.")

    def test_deleteAccountFail(self):
        # Eligible user logged in, deleting nonexistent account
        result = self.app.command("deleteAccount username")
        self.assertEquals(result, "Account {username} does not exist!")

        # Administrator logged in, deleting administrator or supervisor account
        result = self.app.command("deleteAccount username")
        self.assertEquals(result, "Permission denied - your role may not delete accounts of these type!")

        # Ineligible user logged in, deleting account of any role
        result = self.app.command("createAccount username")
        self.assertEquals(result, "Account {username} deleted successfully.")

    def test_createCourseSuccess(self):
        # Eligible user logged in, create course
        result = self.app.command("createCourse courseName department courseNumber")
        self.assertEquals(result, "Course {courseName} created successfully.")

    def test_createCourseFail(self):
        # Eligible user logged in, create duplicate course
        result = self.app.command("createCourse courseName department courseNumber")
        self.assertEquals(result, "Course {courseName} already exists!")

        # Ineigible user logged in, create course
        result = self.app.command("createCourse courseName department courseNumber")
        self.assertEquals(result, "Permission Denied - Your role may not create courses!")

    def test_sendEmailSuccess(self):
        # Email is sent to the proper groups. No issues
        result = self.app.command("sendEmail group student content")
        self.assertEqual(result, "Successfully sent.")

    def test_sendEmailFailure(self):
        # Email failure is sent back to individual if they send an email to a group they should not be able to
        result = self.app.command("sendEmail group student content")
        self.assertEqual(result, "Permission denied - your role may not send email to that group.")

    def test_assignInstructorSuccess(self):
        # Supervisors only - Successfully adds an instructor (that already exists) to a course
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Successfully added (instructor) to (course)")

    def test_assignInstructorPermissionDenied(self):
        # User who is not a supervisor tries to add an instructor to a course
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Permission denied - your role may not add instructors to courses")

    def test_assignInvalidInstructorToCourse(self):
        # Supervisor only - tries to assign an instructor that doesn't exist to a course
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Account (instructor) does not exist")

    def test_assignInstructorToInvalidCourse(self):
        # Supervisors only - tries to add instructor to unassigned course.
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Course (course) does not exist")

    def test_removeInstructorSuccess(self):
        # Supervisors only - Successfully removes an instructor (that already exists) from a course
        result = self.app.command("removeInstructor instructor course")
        self.assertEqual(result, "Successfully removed (instructor) from (course)")

    def test_removeInstructorPermissionDenied(self):
        # User who is not a supervisor tries to remove an instructor from a course
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Permission denied - your role may not remove instructors from courses")

    def test_removeInvalidInstructorFromCourse(self):
        # Supervisor only - tries to remove an instructor that doesn't exist from a course
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Account (instructor) does not exist")

    def test_removeInstructorFromInvalidCourse(self):
        # Supervisors only - tries to remove instructor from unassigned course.
        result = self.app.command("assignInstructor instructor course")
        self.assertEqual(result, "Course (course) does not exist")

    def test_assignTAToCourseSuccess(self):
        # Supervisors only - Successfully adds a TA to a course
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Successfully added (TA) to (course)")

    def test_assignTAToCoursePermissionDenied(self):
        # User who is not a supervisor tries to add a TA to a course
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Permission denied - your role may not add TA's to courses")

    def test_assignInvalidTAToCourse(self):
        # Supervisor only - tries to add a TA that doesn't exist to a course
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Account (TA) does not exist")

    def test_assignTAToInvalidCourse(self):
        # Supervisor only - tries to add a TA to a course that doesn't exist
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Course (course) does not exist")

    def test_removeTAFromCourseSuccess(self):
        # Supervisors only - Successfully removes a TA from a course
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Successfully removed (TA) from (course)")

    def test_removeTAFromCoursePermissionDenied(self):
        # User who is not a supervisor tries to remove a TA from a course
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Permission denied - your role may not remove TA's from courses")

    def test_removeInvalidTAFromCourse(self):
        # Supervisor only - tries to remove a TA that doesn't exist from a course
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Account (TA) does not exist")

    def test_removeTAFromInvalidCourse(self):
        # Supervisor only - tries to remove a TA from a course that doesn't exist
        result = self.app.command("assignTACourse TA course")
        self.assertEqual(result, "Course (course) does not exist")

    def test_assignTAToLabSuccess(self):
        # Supervisor or Instructor - Successfully assigns a TA to a course
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Successfully added (TA) to (lab)")

    def test_assignTAToLabPermissionDenied(self):
        # User tries to add TA to lab permission denied
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Permission denied - your role may not add TAs to lab sections")

    def test_assignInvalidTAToLab(self):
        # Supervisor only - tries to add a TA that doesn't exist to a course
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Account (TA) does not exist")

    def test_assignTAToInvalidLab(self):
        # Supervisor only - tries to add TA to a lab that doesn't exist
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Lab section (lab) does not exist")

    def test_removeTAFromLabSuccess(self):
        # Supervisor or Instructor - Successfully removes a TA from a course
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Successfully removed (TA) from (lab)")

    def test_removeTAFromLabPermissionDenied(self):
        # User tries to remove TA from lab permission denied
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Permission denied - your role may not remove TAs from lab sections")

    def test_removeInvalidTAFromLab(self):
        # Supervisor only - tries to remove a TA that doesn't exist from a course
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Account (TA) does not exist")

    def test_removeTAFromInvalidLab(self):
        # Supervisor only - tries to remove TA from a lab that doesn't exist
        result = self.app.command("assignTALab TA lab")
        self.assertEqual(result, "Lab section (lab) does not exist")

    def test_editOwnContactInfoSuccess(self):
        # User successfully edits a field in their contact info
        result = self.app.command("editOwnContactInfo field revision")
        self.assertEqual(result, "(field) successfully revised")

    def test_editOwnContactInfoFieldDoesNotExist(self):
        # User failures to edit a field in their contact info because it doesn't exist
        result = self.app.command("editOwnContactInfo field revision")
        self.assertEqual(result, "Field (field) does not exist")

    def test_readTAAssignmentSuccess(self):
        # User reads TA assignments
        result = self.app.command("readTAAssignment TA")
        self.assertEqual(result, "(ta) info (info)")

    def test_resdTAAssignmentFailure(self):
        # User tries to look at a TA that doesn't exist
        result = self.app.command("readTAAssignment TA")
        self.assertEqual(result, "TA (ta) doesn't exist")

    def test_readAllTAAssignment(self):
        # User reads all TA Assignments
        result = self.app.command("readAllTAAssignments")
        self.assertEqual(result, "TA info (info)")

    def test_readPublicContactInfoSuccess(self):
        # User reads contact info for another user
        result = self.app.command("readPublicContactInfo user field")
        self.assertEqual(result, "Public info (info)")

    def test_readPublicContactInfoFailure(self):
        # User unable to read contact info on invalid user
        result = self.app.command("readPublicContactInfo user field")
        self.assertEqual(result, "User (user) does not exist.")
