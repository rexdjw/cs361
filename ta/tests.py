from django.test import TestCase
from users.models import Users
from ta.models import TA


class TestTA(TestCase):

    def setUp(self):
        self.users = Users.objects.create(username="testUser")
        self.ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=1)

    def test_constructor_1(self):
        tc1 = TA.objects.create(account=self.users, graderStatus=True, numberOfLabs=4)
        self.assertEqual(tc1.graderStatus, True)
        self.assertEqual(tc1.numberOfLabs, 4)

    def test_constructor_2(self):
        tc2 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=9)
        self.assertEqual(tc2.graderStatus, False)
        self.assertEqual(tc2.numberOfLabs, 9)

    def test_constructor_3(self):
        tc3 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=9.4)
        self.assertEqual(tc3.graderStatus, False)
        self.assertEqual(tc3.numberOfLabs, 9.4)

    def test_constructor_4(self):
        tc4 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=4)
        self.assertEqual(tc4.graderStatus, False)
        self.assertEqual(tc4.numberOfLabs, 4)

    def test_constructor_5(self):
        tc5 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=-4)
        self.assertEqual(tc5.graderStatus, False)
        self.assertEqual(tc5.numberOfLabs, -4)

    def test_constructor_6(self):
        tc6 = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=0)
        self.assertEqual(tc6.graderStatus, False)
        self.assertEqual(tc6.numberOfLabs, 0)

    # Test setTAStatus
    def test_setTAStatus_1(self):
        TA.set_ta_status(self.users, grader_status=False, number_of_labs=0)
        self.assertEqual(self.users.grader_status, False)
        self.assertTrue(self.users.number_of_labs == 0)

    def test_setTAStatus_2(self):
        TA.set_ta_status(self.users, grader_status=True, number_of_labs=0)
        self.assertFalse(self.users.grader_status is False)
        self.assertTrue(self.users.number_of_labs == 0)

    def test_setTAStatus_3(self):
        with self.assertRaises(ValueError):
            TA.set_ta_status(self.users, grader_status=True, number_of_labs=-5)

    def test_setTAStatus_4(self):
        with self.assertRaises(ValueError):
            TA.set_ta_status(self.users, grader_status=True, number_of_labs=0.4)

    def test_setTAStatus_5(self):
        with self.assertRaises(ValueError):
            TA.set_ta_status(self.users, grader_status="Hello", number_of_labs=0)

    def test_setTAStatus_6(self):
        with self.assertRaises(ValueError):
            TA.set_ta_status(self.users, grader_status='G', number_of_labs=4)

    def test_setTAStatus_7(self):
        with self.assertRaises(ValueError):
            TA.set_ta_status(self.users, grader_status=9, number_of_labs=2)

    def test_setTAStatus_8(self):
        with self.assertRaises(ValueError):
            TA.set_ta_status(self.users, grader_status=True, number_of_labs='r')

    def test_setTAStatus_9(self):
        with self.assertRaises(ValueError):
            TA.set_ta_status(self.users, grader_status=False, number_of_labs="Hi")

    def test_setTAStatus_10(self):
        with self.assertRaises(ValueError):
            TA.set_ta_status(self.users, grader_status=False, number_of_labs=False)

