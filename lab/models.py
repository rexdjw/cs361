from django.db import models

# Create your models here.
class Lab(models.Model):
    labNumber = models.IntegerField()

    @classmethod
    def create(cls, lab_number, ta = None):
        """create lab object with optionally assigned ta

        requires supervisor permissions

        :param lab_number:int
        :param ta:TA
        """

        # check permissions - TODO

        cls.lab_number = lab_number
        cls.ta = ta


    def assign_ta(self, ta):
        """assign TA to this lab section

        requires permissions of instructor assigned to this course or supervisor

        :param ta:TA
        :return:None
        """
        # check permissions - TODO

        self.ta = ta

    def remove_ta(self):
        """remove TA from this lab section

        if no TA is assigned to this section return false, else remove and return true

        requires permissions of instructor assigned to this course or supervisor

        :return:Boolean
        """
        # check permissions - TODO

        if self.ta is None:
            return False
        else:
            self.ta = None
            return True