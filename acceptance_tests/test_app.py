from unittest import TestCase, TestSuite, TextTestRunner, makeSuite
from app import App


class TestApp(TestCase):

    def setUp(self):
        self.app = App()

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
