from django.db import models


# Create your models here.
from users.models import Users


class TA(models.Model):
    graderStatus = models.BooleanField()
    numberOfLabs = models.IntegerField()
    account = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

    @classmethod
    def create(cls, account, grader_status=None, number_of_labs=None):
        """Create a TA object, optionally specifying grader status and number of labs
        requires supervisor permissions
        :param account:User
        :param grader_status:Boolean
        :param number_of_labs:Int
        """

        return cls(account=account, graderStatus=grader_status, numberOfLabs=number_of_labs)

    def set_ta_status(self, grader_status, number_of_labs):
        """Set a TA's grader status and number of labs
        :param grader_status: Boolean
        :param number_of_labs: Int
        :return:Void
        """

        # Only populate grader_status if it's a boolean (TODO: DEFAULT FALSE???)
        if isinstance(grader_status, bool):
            self.grader_status = grader_status
        else:
            raise ValueError('Grader status input is not valid, please enter True or False.')

        # Only populate number_of_labs if it's an int
        if type(number_of_labs) is int and number_of_labs >= 0:
            self.number_of_labs = number_of_labs
        else:
            raise ValueError('Number of labs input is not valid, please enter a positive integer.')

    def __str__(self):
        return self.account.username