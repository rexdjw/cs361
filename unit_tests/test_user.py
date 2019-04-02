import unittest

from random import randint
from unit_tests.users import Users


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = Users()

    def tearDown(self):
        self.user.dispose()
        self.user = None

    def test_create_account(self):

        self.user.create_account("jayson", "12345", 8)

        self.assertTrue(self.user.username == "jayson")
        self.assertFalse(self.user.username == "12345")

    def test_delete_account(self):

        self.user.delete_account()
        self.assertEqual(self.user.username, None)

    def test_delete_and_create_account(self):

        self.user.create_account("Sean", "1234", 8)

        self.assertEqual("Sean", self.user.username)
        self.assertFalse(self.user.password == "12345")

        self.user.delete_account()

        self.assertEqual(None, self.user.username)
        self.assertNotEqual("Sean", self.user.username)

    def test_is_super0(self):

        self.user.create_account("Sean", "1234", randint(0, 15) | 8)
        self.assertTrue(self.user.is_super())

    def test_is_super1(self):

        self.user.create_account("Sean", "1234", randint(0, 15) & 7)
        self.assertFalse(self.user.is_super())

    def test_is_admin0(self):

        self.user.create_account("Sean", "1234", randint(0, 15) | 4)
        self.assertTrue(self.user.is_admin())

    def test_is_admin1(self):

        self.user.create_account("Sean", "1234", randint(0, 15) & 11)
        self.assertFalse(self.user.is_admin())

    def test_is_instructor0(self):

        self.user.create_account("Sean", "1234", randint(0, 15) | 2)
        self.assertTrue(self.user.is_instructor())

    def test_is_instructor1(self):

        self.user.create_account("Sean", "1234", randint(0, 15) & 13)
        self.assertFalse(self.user.is_instructor())

    def test_is_ta0(self):

        self.user.create_account("Sean", "1234", randint(0, 15) | 1)
        self.assertTrue(self.user.is_ta())

    def test_is_ta1(self):

        self.user.create_account("Sean", "1234", randint(0, 15) & 14)
        self.assertFalse(self.user.is_ta())

    def test_edit_account_info(self):
        self.user = Users()

        self.user.create_account("rock", "Ilikeprogramming", 0)

        self.user.reset_username("jrock")
        self.user.reset_password("Ilove361")
        self.user.reset_roles(2)

        self.assertEqual(self.user.username, "jrock")
        self.assertEqual(self.user.password, "Ilove361")
        self.assertEqual(self.user.roles, 2)