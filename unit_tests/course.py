from unit_tests.TA import TA
from unit_tests.users import Users
from unit_tests.lab import Lab


class Course:

    def __init__(self, course_name, department, course_number, instructor=None):
        """create a course object requires course name, department, and course number

        requires Supervisor or Administrator permissions

        :param course_name:string
        :param department:string
        :param course_number:int
        :param instructor:user
        """

        # check permission - TODO
        # Should we check for other
        self.courseName = course_name
        self.department = department
        if course_number.isdigit:
            self.courseNumber = course_number
        else:
            raise ValueError('Course number was not a number')
        self.instructor = instructor

        self.TAs = {}   # Dictionary of TAs where key = username, value = TA object

        self.labs = {}  # Dictionary of Labs where key = lab number, value = TA object

    # createCourse equivalent to constructor? calling createCourse on a course object doesnt make sense

    def assign_instructor(self, instructor):
        """assign an instructor to a course

        requires Supervisor permission

        :param instructor:User

        :return: None
        """

        # check permissions - TODO

        self.instructor = instructor

    def remove_instructor(self):
        """remove assigned instructor from course

        requires Supervisor permissions

        :return: Boolean
        """

        # check permissions - TODO

        # if there is no instructor return false

        if self.instructor is None:
            return False

        # else set instructor to None and return true
        else:
            self.instructor = None
            return True

    def assign_TA(self, ta, grader_status=None, number_of_labs=None):
        """assign TA user to this course with optionally specified grader status and number of labs

        :param ta:User
        :param grader_status:
        :param number_of_labs:
        :return:"""


        # check permission - TODO

        # create TA object with optionally specified grader status and number of labs
        ta_to_add = TA(ta, grader_status, number_of_labs)

        # add TA to self.TAs with username as key, and TA object as value
        self.TAs.update({ta, ta_to_add})



    def remove_TA(self, ta):
        """ remove TA from course

        requires Supervisor permissions
        :param ta:User
        :return:None"""


        # check permissions - TODO

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

    def display_assignment(self):
        """Display instructor and TA's assigned to this course

        no permissions required

        :return:None
        """

        # display how? print out? return?
        # are there permissions associated with this?

        print("Instructor of " + self.courseName + " is " + self.instructor)

        # figure out how to print self.tas dictionary values - TODO
        #print("TAs of " + self.courseName + " are " + self.TAs)
        for keys, values in self.TAs.items():
            print(keys + " " + values)

    def create_lab_section(self, lab_number, ta = None):
        """create_lab_section and assign it to this course

        requires supervisor permissions

        :param lab_number:int
        :param ta:TA
        :return:None"""

        # check permissions - TODO

        # create lab section for this course with lab number, and optionally specified assigned TA
        lab_section = Lab(lab_number, ta)

        # add Lab to self.labs with lab number as key, and Lab object as value
        self.TAs.update({lab_number, lab_section})


