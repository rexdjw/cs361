
class ContactInfo:

    def __init__(self, name="", phone_number="", email="", address="", office_hours="", office_number=""):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.office_hours = office_hours
        self.office_number = office_number

    def edit_contact_info(self, name=None, phone_number=None, email=None, address=None, office_hours=None, office_number=None):
        pass

    def get_public(self):
        return [self.name, self.email, self.office_hours, self.office_number]

    def get_private(self):
        return [self.phone_number, self.address]

