from django.test import TestCase

from contactinfo.models import ContactInfo
from users.models import Users


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
