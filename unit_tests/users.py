class Users:

    def __init__(self, username=None, password=None, roles=0, contact_info=None):
        """create a course object requires course name, department, and course number

        requires Supervisor or Administrator permissions

        :param username:string
        :param password:string
        :param roles:int in range 0-15
        :param contact_info:contact_info
        """
        self.username = username
        self.password = password
        self.roles = roles
        self.contact_info = contact_info
        # todo: validate roles input

    def create_account(self, username, password, roles):
        """create a new user object and add it to the database

        :param username:string
        :param password:string
        :param roles:int in range 0-15
        """
        self.username = username
        self.password = password
        self.roles = roles
        # todo: validate roles input
        # todo: add to db

    def delete_account(self):
        """remove this user object from the db"""
        self.username = None
        self.password = None
        self.contact_info = None
        self.roles = 0
        # todo: remove from db

    def reset_username(self, new_username):
        """change the username of this user object

        :param new_username:string
        """
        self.username = new_username

    def reset_password(self, new_password):
        """change the password of this user object

        :param new_password:string
        """
        self.password = new_password

    def reset_roles(self, new_roles):
        """change the roles of this user object

        :param new_roles:int in range 0-15
        """
        #todo: validate roles input
        self.roles = new_roles

    def is_super(self):
        """query whether this user object has supervisor permission"""
        return (self.roles & 8) == 8

    def is_admin(self):
        """query whether this user object has administrator permission"""
        return (self.roles & 4) == 4

    def is_instructor(self):
        """query whether this user object has instructor permission"""
        return (self.roles & 2) == 2

    def is_ta(self):
        """query whether this user object has ta permission"""
        return (self.roles & 1) == 1

    def display_assignments(self, role):
        # todo: if instructor, display assigned courses
        # todo: if ta, display assigned courses and labs
        pass

    @staticmethod
    def display_users(self, role=None):
        # todo: display a list of all users
        # todo: if role is not None, display all users with specified role
        pass

    def dispose(self):
        # todo: ???
        pass