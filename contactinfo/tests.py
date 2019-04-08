from django.test import TestCase

from contactinfo.models import ContactInfo
from users.models import Users


class TestContactInfo(TestCase):
    def testInit(self):
        users = Users.objects.create(username="testUser")

        ci = ContactInfo.objects.create(account=users, name="myName", phoneNumber="4145551234",
                                        email="foo@uwm.edu", address="1234 Street St, Milwaukee, WI, 53211")
        self.assertEqual("myName", ci.name)
        self.assertEqual("4145551234", ci.phoneNumber)
        self.assertEqual("foo@uwm.edu", ci.email)
        self.assertEqual("1234 Street St, Milwaukee, WI, 53211", ci.address)
        self.assertEqual("", ci.officeHours)
        self.assertEqual("", ci.officeNumber)

    def testGetPublic(self):
        users = Users.objects.create(username="testUser")
        ci = ContactInfo.objects.create(account=users, name="myName", phoneNumber="4145551234",
                                        email="foo@uwm.edu", address="1234 Street St, Milwaukee, WI, 53211")
        infolist = ci.get_public()
        self.assertEqual(infolist, ["myName", "foo@uwm.edu", "", ""])

    def testGetPrivate(self):
        users = Users.objects.create(username="testUser")
        ci = ContactInfo.objects.create(account=users, name="myName", phoneNumber="4145551234",
                                        email="foo@uwm.edu", address="1234 Street St, Milwaukee, WI, 53211")
        infolist = ci.get_private()
        self.assertEqual(infolist, ["myName", "4145551234", "foo@uwm.edu", "1234 Street St, Milwaukee, WI, 53211", "", ""])
