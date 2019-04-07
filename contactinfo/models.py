from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    phoneNumber = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    officeHours = models.CharField(max_length=32)
    officeNumber = models.CharField(max_length=32)

    @classmethod
    def create(cls, name="", phone_number="", email="", address="", office_hours="", office_number=""):
        cls.name = name
        cls.phone_number = phone_number
        cls.email = email
        cls.address = address
        cls.office_hours = office_hours
        cls.office_number = office_number

    def edit_contact_info(self, name=None, phone_number=None, email=None, address=None, office_hours=None, office_number=None):
        pass

    def get_public(self):
        return [self.name, self.email, self.office_hours, self.office_number]

    def get_private(self):
        return [self.phone_number, self.address]