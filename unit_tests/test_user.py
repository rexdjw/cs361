import unittest

from unit_tests.users import Users


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = Users()

    def tearDown(self):
        self.user.dispose()
        self.user = None

    def test_createAccount(self):

        self.user.createAccount("jayson", "12345", {"Supervisor": True, "Administrator": False, "Instructor": False, "TA": False})

        self.assertTrue(self.user.username == "jayson")
        self.assertFalse(self.user.username == "12345")


    def test_deleteAccount(self):

        self.assertTrue(self.user.deleteAccount("jayson"))
        self.assertEqual(self.user.username == None)



    def test_deleteAndCreateAccount(self):

        self.user.createAccount("Sean", "1234",{"Supervisor": True, "Administrator": False, "Instructor": False, "TA": False})

        self.assertEqual("Sean", self.user.username)
        self.assertFalse(self.user.password == "12345")

        self.user.deleteAccount("Sean")

        self.assertEqual(None, self.user.username)
        self.assertNotEqual("Sean", self.user.username)


    def test_getRoles(self):

        self.user.createAccount("Sean", "1234",{"Supervisor": True, "Administrator": False, "Instructor": False, "TA": False})

        self.assertEqual({"Supervisor": True, "Administrator": False, "Instructor": False, "TA": False}, self.user.getRoles())
        self.assertNotEqual({"Supervisor": False, "Administrator": False, "Instructor": False, "TA": False}, self.user.getRoles())

    def test_editAccountInfo_Edit_All(self):
        instructor = Users()

        instructor.createAccount("rock", "Ilikeprogramming",{"Supervisor": False, "Administrator": True, "Instructor": False, "TA": False})


        instructor.editAccountInfo("rock", "jrock", "Ilove361", {"Supervisor": False, "Administrator": False, "Instructor": True, "TA": False})

        self.assertEqual(instructor.username, "jrock")
        self.assertEqual(instructor.password, "Ilove361")
        self.assertEqual(instructor.accountRoles, {"Supervisor": False, "Administrator": False, "Instructor": True, "TA": False})