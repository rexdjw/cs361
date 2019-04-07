class TA:

    def __init__(self, ta, grader_status=None, number_of_labs=None):
        """Create a TA object, optionally specifying grader status and number of labs
        requires supervisor permissions
        :param ta:User
        :param grader_status:Boolean
        :param number_of_labs:Int
        """

        # TODO: Check that user is valid by querying database (don't know how to do yet)
        self.ta = ta

        # Only populate grader_status if it's a boolean
        if isinstance(grader_status, bool):
            self.grader_status = grader_status
        else:
            # TODO: Ask if we need to do more than print a statement when input is bad
                # Should we fail and terminate so they have to re-do everything?
            raise ValueError('Grader status was not a boolean')

        # Only populate number_of_labs if it's an int
        if isinstance(number_of_labs, int):
            self.number_of_labs = number_of_labs
        else:
            raise ValueError('Number of labs was not an int')

    def set_ta_status(self, grader_status, number_of_labs):
        """Set a TA's grader status and number of labs
        :param grader_status: Boolean
        :param number_of_labs: Int
        :return:Void
        """

        # Only populate grader_status if it's a boolean (TODO: DEFAULT FALSE???)
        if grader_status is not None & isinstance(grader_status, bool):
            self.grader_status = grader_status
        else:
            raise ValueError('Grader status input is not valid, please enter True or False.')

        # Only populate number_of_labs if it's an int
        if isinstance(number_of_labs, int) & number_of_labs >= 0:
            self.number_of_labs = number_of_labs
        else:
            raise ValueError('Number of labs input is not valid, please enter a positive integer.')