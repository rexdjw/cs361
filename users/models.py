from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator

from contactinfo.models import ContactInfo


class UserGroup(models.Model):
    name = models.CharField(max_length=25)
    roles = models.IntegerField()

    class Meta:
        verbose_name_plural = "User Groups"

    def __str__(self):
        return f"{self.name}"


class Users(AbstractUser):
    roles = models.IntegerField(null=True, default=0)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, blank=True, null=True)

    @classmethod
    def list_by_user_group_id(cls, user_group_id):
        return list(cls.objects.filter(user_group__id=user_group_id))

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

    def set_contact_info(self, name, phone_numer, email, address, office_hours=None, office_number=None):
        """set the contact information of a user optionally specifying office hours and office number

        :param name:string
        :param phone_numer:string
        :param email:string
        :param address:string
        :param office_hours:string
        :param office_number:string
        :return:
        """
        self.contact_info = ContactInfo(name, phone_numer, email, address, office_hours, office_number)
        self.save()

    def __str__(self):
        """return this user as a string of format "username, role"

        :return:
        """
        if self.is_super():
            return "username: " + self.username + " - supervisor"
        if self.is_admin():
            return "username: " + self.username + " - administrator"
        if self.is_instructor():
            return "username: " + self.username + " - instructor"
        if self.is_ta():
            return "username: " + self.username + " - TA"
        else:
            return "username: " + self.username + " has no assigned roles!"

