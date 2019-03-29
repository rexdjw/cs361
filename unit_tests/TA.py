class TA:

    def __init__(self, ta, grader_status = None, number_of_labs = None):
        """create a TA object, optionally specifying grader status and number of labs

        requires supervisor permissions

        :param ta:User
        :param grader_status:Boolean
        :param number_of_labs:Int
        """
        self.ta = ta
        self.grader_status = grader_status
        self.number_of_labs = number_of_labs

    def set_ta_status(self, grader_status, number_of_labs):
        """set a TA's grader status and number of labs

        :param grader_status:Boolean
        :param number_of_labs:Int
        :return:None
        """
        self.grader_status = grader_status
        self.number_of_labs = number_of_labs