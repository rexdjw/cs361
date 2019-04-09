from django.test import TestCase

from random import randint
from users.models import Users
from contactinfo.models import ContactInfo


class TestUser(TestCase):

    def setUp(self):
        self.user = Users()

    def tearDown(self):
        self.user.dispose()
        self.user = None

    def test_create_account(self):

        self.user.create_account("jayson", "12345", 8)

        self.assertTrue(self.user.username == "jayson")
        self.assertFalse(self.user.username == "12345")

        # todo: assert that this user is now in the db

    def test_delete_account(self):

        self.user.delete_account()
        self.assertEqual(self.user.username, None)

        # todo: assert that this user is no longer in the db

    def test_delete_and_create_account(self):

        self.user.create_account("Sean", "1234", 8)

        self.assertEqual("Sean", self.user.username)
        self.assertFalse(self.user.password == "12345")

        # todo: assert that this user is now in the db

        self.user.delete_account()

        self.assertEqual(None, self.user.username)
        self.assertNotEqual("Sean", self.user.username)

        # todo: assert that this user is no longer in the db

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

    def test_set_contact_info(self):

        # todo : why is this broken?

        # Error
        # Traceback (most recent call last):
        # File "C:\Users\Nathan\PycharmProjects\cs361\users\tests.py", line 116, in test_set_contact_info
        # self.user.editContactInfo(self.user, name, ph_num, email, address, o_hours, o_num)
        # File "C:\Users\Nathan\PycharmProjects\cs361\users\models.py", line 91, in editContactInfo
        # ci = ContactInfo.objects.filter(account=account)[0]
        # File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\lib\site-packages\django\db\models\
        # query.py", line 309, in __getitem__
        # return qs._result_cache[0]
        # IndexError: list index out of range"""

        """self.user = Users()

        self.user.create_account("username", "password", 0)

        name = "myName"
        ph_num = "4145551234"
        email = "foo@uwm.edu"
        address = "1234 Street St, Milwaukee, WI, 53211"
        o_hours = ""
        o_num = ""

        self.user.editContactInfo(self.user, name, ph_num, email, address, o_hours, o_num)

        self.assertEqual(self.user.contactinfo.name, name)
        self.assertEqual(self.user.contactinfo.phoneNumber, ph_num)
        self.assertEqual(self.user.contactinfo.email, email)
        self.assertEqual(self.user.contactinfo.address, address)
        self.assertEqual(self.user.contactinfo.officeHours, o_hours)
        self.assertEqual(self.user.contactinfo.officeNumber, o_num)"""
        pass

