from unittest import TestCase

from unit_tests.contact_info import ContactInfo

"""from project import Class"""


class TestContactInfo(TestCase):
    def testInit0(self):
        ci = ContactInfo()
        self.assertEqual("", ci.name)
        self.assertEqual("", ci.phone_number)
        self.assertEqual("", ci.email)
        self.assertEqual("", ci.address)
        self.assertEqual("", ci.office_hours)
        self.assertEqual("", ci.office_number)

    def testInit1(self):
        ci = ContactInfo("myName", "4145551234", "foo@uwm.edu", "1234 Street St, Milwaukee, WI, 53211")
        self.assertEqual("myName", ci.name)
        self.assertEqual("4145551234", ci.phone_number)
        self.assertEqual("foo@uwm.edu", ci.email)
        self.assertEqual("1234 Street St, Milwaukee, WI, 53211", ci.address)
        self.assertEqual("", ci.office_hours)
        self.assertEqual("", ci.office_number)

    def testEditContactInfo0(self):
        ci = ContactInfo("myName", "4145551234", "foo@uwm.edu", "1234 Street St, Milwaukee, WI, 53211")
        ci.edit_contact_info()
        self.assertEqual("myName", ci.name)
        self.assertEqual("4145551234", ci.phone_number)
        self.assertEqual("foo@uwm.edu", ci.email)
        self.assertEqual("1234 Street St, Milwaukee, WI, 53211", ci.address)
        self.assertEqual("", ci.office_hours)
        self.assertEqual("", ci.office_number)

    def testEditContactInfo1(self):
        ci = ContactInfo()
        ci.edit_contact_info("myName", "4145551234", "foo@uwm.edu", "1234 Street St, Milwaukee, WI, 53211")
        self.assertEqual("myName", ci.name)
        self.assertEqual("4145551234", ci.phone_number)
        self.assertEqual("foo@uwm.edu", ci.email)
        self.assertEqual("1234 Street St, Milwaukee, WI, 53211", ci.address)
        self.assertEqual("", ci.office_hours)
        self.assertEqual("", ci.office_number)

    def testEditContactInfo2(self):
        ci = ContactInfo()
        ci.edit_contact_info()
        self.assertEqual("", ci.name)
        self.assertEqual("", ci.phone_number)
        self.assertEqual("", ci.email)
        self.assertEqual("", ci.address)
        self.assertEqual("", ci.office_hours)
        self.assertEqual("", ci.office_number)

    def testGetPublic0(self):
        ci = ContactInfo()
        infolist = ci.get_public()
        self.assertEqual(infolist, ["", "", "", ""])

    def testGetPublic1(self):
        ci = ContactInfo("myName", "4145551234", "foo@uwm.edu", "1234 Street St, Milwaukee, WI, 53211")
        infolist = ci.get_public()
        self.assertEqual(infolist, ["myName", "4145551234", "foo@uwm.edu", "1234 Street St, Milwaukee, WI, 53211"])

    def testGetPrivate0(self):
        ci = ContactInfo()
        infolist = ci.get_private()
        self.assertEqual(infolist, ["", ""])

    def testGetPrivate1(self):
        ci = ContactInfo("myName", "4145551234", "foo@uwm.edu", "1234 Street St, Milwaukee, WI, 53211", "9-11TR",
                         "EMS371")
        infolist = ci.get_private()
        self.assertEqual(infolist, ["9-11TR", "EMS371"])
