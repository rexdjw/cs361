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
        self.update_grader_status(grader_status)
        self.update_number_labs(number_of_labs)
        self.save()

    def update_grader_status(self, graderStatus):

        self.grader_status = graderStatus
        self.save()

    def update_number_labs(self, labs):

        self.number_of_labs = labs
        self.save()

    def __str__(self):
        return self.account.username