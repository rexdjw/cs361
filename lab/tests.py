from django.test import TestCase
from lab.models import Lab
from users.models import Users
from ta.models import TA


class TestLab(TestCase):

    def setUp(self):
        self.users = Users.objects.create(username="testUser")
        self.ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=1)

    """
    def test_constructor_1(self):
        with self.assertRaises(ValueError):
            Lab.objects.create(labNumber=-800)
    """

    def test_constructor_2(self):
        lab = Lab.objects.create(labNumber=400)
        self.assertEqual(lab.labNumber, 400)

    def test_constructor_3(self):
        with self.assertRaises(ValueError):
            Lab.objects.create(labNumber="hello")

    def test_assign_TA_1(self):
        lab = Lab.objects.create(labNumber=401)
        lab.assign_TA(self.ta)
        self.assertEqual(lab.TAs.get(account=self.users), self.ta)

    def test_assign_TA_2(self):
        lab = Lab.objects.create(labNumber=401)
        ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=0)
        lab.assign_TA(ta)
        self.assertEqual(lab.TAs.get(account=self.users), ta)

    def test_assign_TA_3(self):
        lab = Lab.objects.create(labNumber=401)
        ta = TA.objects.create(account=self.users, graderStatus=True, numberOfLabs=10)
        lab.assign_TA(ta)
        self.assertEqual(lab.TAs.get(account=self.users), ta)

