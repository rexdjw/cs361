from django.test import TestCase

from random import randint
from users.models import Users


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

    def test_to_string1(self):
        Users.create("username", "password", 10).save()
        self.user = Users.objects.get(username="username")

        self.assertEqual(str(self.user), "User username has [Supervisor] [Instructor] role permissions.")
