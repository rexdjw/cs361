from django.db import models


class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    phoneNumber = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    officeHours = models.CharField(max_length=32)
    officeNumber = models.CharField(max_length=32)


class Users(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16, min_length=8)
    accountRoles = models.IntegerField()
    contactInfo = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)


class TA(models.Model):
    graderStatus = models.BooleanField()
    numberOfLabs = models.IntegerField()
    TA = models.ForeignKey(Users, on_delete=models.CASCADE)


class Lab(models.Model):
    labNumber = models.IntegerField()
    TA = models.ForeignKey(TA, on_delete=models.CASCADE)


class Course(models.Model):
    courseName = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    courseNumber = models.IntegerField()
    instructor = models.ForeignKey(Users, on_delete=models.CASCADE)
    TAs = models.ManyToOneRel(TA)
    labs = models.ManyToOneRel(Lab)
