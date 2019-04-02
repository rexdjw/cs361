import unittest
from ta import TA


# How are we querying the database - need to check validity of ta user object
# Do we have a max number of lab sections a TA can have

class TestTA(unittest.TestCase):

    def test_constructor_1(self):
        # TODO: User parameter?
        tc1 = TA(self, ta="", grader_status=True, number_of_labs=4)
        self.assertEqual(tc1.grader_status, True)
        self.assertEqual(tc1.number_of_labs, 4)

    def test_constructor_2(self):
        # TODO: User parameter?
        tc2 = TA(self, ta="", grader_status=None, number_of_labs=9)
        self.assertEqual(tc2.grader_status, None)
        self.assertEqual(tc2.number_of_labs, 9)

    def test_constructor_3(self):
        # TODO: User parameter?
        tc3 = TA(self, ta="", grader_status=None, number_of_labs=9.4)
        # Not sure if this will work, ask
        self.assertEqual(tc3.grader_status, None)
        self.assertRaises(ValueError)

    def test_constructor_4(self):
        # TODO: User parameter?
        tc4 = TA(self, ta="", grader_status=False, number_of_labs=4)
        self.assertEqual(tc4.grader_status, False)
        self.assertEqual(tc4.number_of_labs, 4)

    # TODO: Test with invalid user ta objects (will need to query database)
    # TODO: Test with maxed out number of lab sections

    # TODO: Test setTAStatus
    def test_setTAStatus_1(self):
        TA.set_ta_status(False, 10)
        # TODO: Pass

    def test_setTAStatus_2(self):
        TA.set_ta_status(ta, True, 10)
        # TODO: Pass

    def test_setTAStatus_3(self):
        TA.set_ta_status(ta, None, -5)
        # TODO: Assert error
        self.assertRaises(ValueError)

    def test_setTAStatus_4(self):
        TA.set_ta_status(ta, False, 0.4)
        # TODO: Assert error
        self.assertRaises(ValueError)

    def test_setTAStatus_5(self):
        TA.set_ta_status(ta, "Hello", 4)
        self.assertRaises(ValueError)

    def test_setTAStatus_6(self):
        TA.set_ta_status(ta, 'G', 9)
        # TODO: Assert error
        self.assertRaises(ValueError)

    def test_setTAStatus_7(self):
        TA.set_ta_status(ta, 8, 9)
        # TODO: Assert error
        self.assertRaises(ValueError)
