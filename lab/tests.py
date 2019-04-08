from django.test import TestCase

from lab.models import Lab
from users.models import Users
from ta.models import TA


class TestLab(TestCase):

    def setUp(self):
        self.users = Users.objects.create(username="testUser")
        self.ta = TA.objects.create(account=self.users, graderStatus=False, numberOfLabs=1)

    def test_init_with_instructor(self):
        lab = Lab.objects.create(labNumber=401)
        self.assertEqual(lab.labNumber, 401)

    def test_assign_TA(self):
        lab = Lab.objects.create(labNumber=401)
        #self.assertEqual(lab.ta, None)

        #lab.assign_ta(self.ta)
        #self.assertEqual(lab.ta, self.ta)

    def test_remove_TA(self):
        lab = Lab(lab_number=401, ta=self.ta)
        #self.assertEqual(lab.ta, self.ta)

        #lab.remove_ta()
        #self.assertEqual(lab.ta, None)
