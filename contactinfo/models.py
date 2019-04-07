from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    phoneNumber = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    officeHours = models.CharField(max_length=32)
    officeNumber = models.CharField(max_length=32)
    account = models.ForeignKey('users.Users', on_delete=models.DO_NOTHING)


    @classmethod
    def create(cls, name, phone_number, email, address, office_hours=None, office_number=None):
        """Create a ContactInfo object with optionally specified office hours, and office number

        Requires permissions of supervisor or of the user associated with this contact information

        :param name:string
        :param phone_number:string
        :param email:string
        :param address:string
        :param office_hours:string
        :param office_number:string
        :return:None
        """

        cls.name = name
        cls.phone_number = phone_number
        cls.email = email
        cls.address = address
        cls.office_hours = office_hours
        cls.office_number = office_number

    def editContactInfo(self, name=None, phone_number=None, email=None, address=None, office_hours=None,
                        office_number=None):
        """Edit contact information specifying desired fields

        Requires permissions of supervisor or of the user associated with this contact information

        :param name:string
        :param phone_number:string
        :param email:string
        :param address:string
        :param office_hours:string
        :param office_number:string
        :return:None
        """
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.office_hours = office_hours
        self.office_number = office_number
        self.save()

    def get_public(self):
        """Return public contact information which includes - name, email, office hours, office number

        No permissions required

        :return:List[string]
        """
        return [self.name, self.email, self.office_hours, self.office_number]

    def get_private(self):
        """Return private contact information which includes all fields

        Requires Supervisor or Administrator permissions

        :return:List[String]
        """
        return [self.name, self.phone_number, self.email, self.address, self.office_hours, self.office_number]

    def __str__(self):
        """Return this contact information object as a string, which includes publicly available contact information

        :return:
        """
        return self.get_public()

