from unittest import TestCase, TestSuite, TextTestRunner, makeSuite

from unit_tests.test_contact_info import TestContactInfo
from unit_tests.test_user import TestUser
from unit_tests.test_course import TestCourse

suite = TestSuite()
suite.addTest(makeSuite(TestContactInfo))
suite.addTest(makeSuite(TestUser))
runner = TextTestRunner()
res=runner.run(suite)