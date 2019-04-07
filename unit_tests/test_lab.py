import unittest
from unit_tests.lab import Lab
from unit_tests.users import Users
from unit_tests.TA import TA


class TestLab(unittest.TestCase):

    def setUp(self):
        self.users = Users("testUser", "12345")
        self.ta = TA(ta=self.users, grader_status=False, number_of_labs=1)

    def test_init_with_instructor(self):
        lab = Lab(lab_number=401, ta=self.ta)
        self.assertEqual(lab.lab_number, 401)
        self.assertEqual(lab.ta, self.ta)

    def test_assign_TA(self):
        lab = Lab(lab_number=401)
        self.assertEqual(lab.ta, None)

        lab.assign_ta(self.ta)
        self.assertEqual(lab.ta, self.ta)

    def test_remove_TA(self):
        lab = Lab(lab_number=401, ta=self.ta)
        self.assertEqual(lab.ta, self.ta)

        lab.remove_ta()
        self.assertEqual(lab.ta, None)

