from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator

class Users(AbstractUser):
    roles = models.IntegerField(null=True)


    @classmethod
    def create(cls, username=None, password=None, roles=0, contact_info=None):
        """create a course object requires course name, department, and course number

        :param username:string
        :param password:string
        :param roles:int in range 0-15
        :param contact_info:contact_info
        """
        cls.username = username
        cls.password = password
        cls.roles = roles
        cls.contact_info = contact_info

    @staticmethod
    def display_users(role=None):
        """display all users in the database, or all users of the specified role if provided

        this is provided as a static method since it is not particular to any given user

        :param role:int in range 0-15
        """
        # todo: return a list of all users
        # todo: if role is not None, return all users with specified role
        pass

    def create_account(self, username, password, roles):
        """create a new user object and add it to the database

        :param username:string
        :param password:string
        :param roles:int in range 0-15
        """
        self.username = username
        self.password = password
        self.roles = roles
        self.save()

    def delete_account(self):
        """remove this user object from the db and voids all fields"""
        self.username = None
        self.password = None
        self.roles = None
        self.contact_info = None
        # todo: query db for this username - if it exists, remove it

    def display_assignments(self, role):
        # todo: if instructor, display assigned courses
        # todo: if ta, display assigned courses and labs
        pass

    def dispose(self):
        # todo: what is this?
        pass

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
        self.roles = new_roles
