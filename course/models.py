from django.db import models

# Create your models here.
from lab.models import Lab



class Course(models.Model):
    courseName = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    courseNumber = models.IntegerField()
    instructor = models.ForeignKey('users.Users', null=True, on_delete=models.DO_NOTHING)
    labs = models.ManyToManyField(Lab)



    @classmethod
    def create(cls, course_name, department, course_number, instructor=None):
        """create a course object requires course name, department, and course number

        requires Supervisor or Administrator permissions

        :param course_name:string
        :param department:string
        :param course_number:int
        :param instructor:user
        """
        return cls(courseName =course_name, department=department, courseNumber=course_number, instructor=instructor)

    def assign_instructor(self, instructor):
        """assign an instructor to a course

        requires Supervisor permission

        :param instructor:User

        :return: None
        """

        self.instructor = instructor
        self.save()

    def remove_instructor(self):
        """remove assigned instructor from course

        requires Supervisor permissions

        :return: Boolean
        """

        # if there is no instructor return false

        if self.instructor is None:
            return False

        # else set instructor to None and return true
        else:
            self.instructor = None
            return True

    def display_assignment(self):
        """Display instructor and TA's assigned to this course

        no permissions required

        :return:None
        """

        # display how? print out? return?
        # are there permissions associated with this?

        print("Instructor of " + self.course_name + " is " + self.instructor)

        for x in self.TAs.keys():
            print("TA of is " + (self.TAs.get(x)).ta.username)

    def create_lab_section(self, lab_number, ta=None):
        """create_lab_section and assign it to this course

        requires supervisor permissions

        :param lab_number:int
        :param ta:TA
        :return:None"""

        # create lab section for this course with lab number, and optionally specified assigned TA
        lab_section = Lab(lab_number, ta)

        # add Lab to self.labs with lab number as key, and Lab object as value
        self.labs.update({lab_number: lab_section})

    def __str__(self):
        return self.courseName


