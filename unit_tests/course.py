import TA
import users

class Course:

    def __init__(self, course_name=None, department=None, course_number=None, instructor=None):
        """create a course object

        requires Supervisor or Administrator permissions

        :param course_name:string
        :param department:string
        :param course_number:int
        :param instructor:user
        """

        # check permission - TODO

        self.courseName = course_name
        self.department = department
        self.courseNumber = course_number
        self.instructor = instructor

        self.TAs = {}

        self.labs = {}

    # createCourse equivalent to constructor? calling createCourse on a course object doesnt make sense
    # figure out how to check permissions in constructor - create course requires Supervisor or Administrator permissions

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

    def assign_TA(self, ta, grader_status = None, number_of_labs = None):
        """assign TA user to this course with optionally specified grader status and number of labs

        :param ta:User
        :param grader_status:
        :param number_of_labs:
        :return:
        """

        # check permission - TODO

        # create TA object with optionally specified grader status and number of labs
        ta_to_add = TA(ta, grader_status, number_of_labs)

        # add TA to self.TAs with username as key, and TA object as value
        self.TAs.update({ta.username, ta_to_add})



    def remove_TA(self, ta):
        """ remove TA from course

        requires Supervisor permissions
        :param ta:User
        :return:None
        """

        # check permissions - TODO

        # use username of ta to remove as key
        username_to_remove = ta.username

        # search TAs dictionary for this course by username of ta to remove as key
        # remove TA if present and return true
        if 'username_to_remove' in self.TAs:
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

        # figure out how to print TAs dictionary value - TODO
        print("TAs of " + self.courseName + " are " + self.TAs)



