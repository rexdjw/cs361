from django.db import models

# Create your models here.
from ta.models import TA


class Lab(models.Model):
    labNumber = models.IntegerField()
    TAs = models.ManyToManyField(TA)

    @classmethod
    def create(cls, lab_number):
        """create lab object with optionally assigned ta

        requires supervisor permissions

        :param lab_number:int
        :param ta:TA
        """

        return cls(labNumber=lab_number)


    def assign_TA(self, ta):
        """assign TA user to this course with optionally specified grader status and number of labs
        :param ta:User
        :param grader_status:
        :param number_of_labs:
        :return:"""

        self.TAs.add(ta)
        self.save()

    def remove_TA(self, ta):
        """ remove TA from course

        requires Supervisor permissions
        :param ta:User
        :return:None"""

        # use username of ta to remove as key
        username_to_remove = ta.username

        # search TAs dictionary for this course by username of ta to remove as key
        # remove TA if present and return true
        if username_to_remove in self.TAs:
            del self.TAs[username_to_remove]
            return True

        # else return false
        else:
            return False

    def __str__(self):
        return str(self.labNumber)