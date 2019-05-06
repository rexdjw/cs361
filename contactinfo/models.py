from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    phoneNumber = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    officeHours = models.CharField(max_length=32)
    officeNumber = models.CharField(max_length=32)
    account = models.OneToOneField('users.Users', on_delete=models.CASCADE)


    @classmethod
    def create(cls, account, name="", phone_number="<not specified>", email="<not specified>", address="<not specified>", officeHours="<not specified>",
               officeNumber="<not specified>"):
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

        from users.models import Users
        account = Users.objects.get(username=account)
        return cls(account=account, name=name, phoneNumber=phone_number, email=email, address=address, officeHours=officeHours, officeNumber=officeNumber)

    def updateName(self, newName):

        self.name = newName
        self.save()

    def updateEmail(self, newEmail):

        self.email = newEmail
        self.save()

    def updateOfficeHours(self, newHours):

        self.officeHours = newHours
        self.save()

    def updateOfficeNumber(self, newOfficeNumber):

        self.officeNumber = newOfficeNumber
        self.save()

    def updatePhoneNumber(self, newPhone):

        self.phoneNumber = newPhone
        self.save()

    def updateAddress(self, newAddress):

        self.address = newAddress
        self.save()

    def get_public(self):
        """Return public contact information which includes - name, email, office hours, office number

        No permissions required

        :return:List[string]
        """
        return [self.name, self.email, self.officeHours, self.officeNumber]

    def get_private(self):
        """Return private contact information which includes all fields

        Requires Supervisor or Administrator permissions

        :return:List[String]
        """
        return [self.name, self.phoneNumber, self.email, self.address, self.officeHours, self.officeNumber]


    def __str__(self):
        """Return this contact information object as a string, which includes publicly available contact information

        :return:
        """
        return str(self.get_public())

