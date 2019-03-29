class Course:

    def __init__(self, courseName=None, department=None, courseNumber=None, instructor=None, TAs=None, labs=None):
        self.courseName = courseName
        self.department = department
        self.courseNumber = courseNumber
        self.instructor = instructor

        # figure out how to include multiple objects in field
        self.TAs = TAs

        # figure out how to include multiple objects in field
        self.labs = labs

    # createCourse equivalent to constructor? calling createCourse on a course object doesnt make sense
    # figure out how to check permissions in constructor - create course requires Supervisor or Administrator permissions

    def assignInstructor(self, instructor):
        '''assign an instructor to a course

        requires Supervisor permission

        :param instructor:User

        :return: None
        '''

        # check permissions
        self.instructor = instructor

    def removeInstructor(self):
        '''remove assigned instructor from course

        requires Supervisor permissions

        :return: Boolean
        '''

        # check permissions
        if (self.instructor == None):
            return False
        else:
            self.instructor = None
            return True

    def assignTA(self, TA):
        '''assign a TA to a course

        requires Supervisor permissions



        :param TA:User
        :return: None
        '''

        # check permission

        # add TA to self.TAs

    def removeTA(self, TA):
        ''' remove TA from course

        requires Supervisor permissions
        :param TA:User
        :return:None
        '''

        # check permissions

        # if TAs assigned to this course include TA
        # remove TA and return true
        # else return false


    # doesn't make sense to have displayCourses() in course class?

    def displayAssignment(self):
        '''Display instructor and TA's assigned to this course

        no permissions required

        :return:None
        '''

        # display how? print out? return?
        # are there permissions associated with this?

        print("Instructor of " + self.courseName + " is " + self.instructor)
        print("TAs of " + self.courseName + " are " + self.TAs)



