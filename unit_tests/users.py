class Users:

    def __init__(self, username=None, password=None, roles=0, contact_info=None):
        self.username = username
        self.password = password
        self.roles = roles
        self.contact_info = contact_info

    def create_account(self, username, password, roles):
        self.username = username
        self.password = password
        self.roles = roles

    def delete_account(self):
        self.username = None
        self.password = None
        self.contact_info = None
        self.roles = 0

    def reset_username(self, new_username):
        self.username = new_username

    def reset_password(self, new_password):
        self.password = new_password

    def reset_roles(self, new_roles):
        self.roles = new_roles

    def is_super(self):
        return (self.roles & 8) == 8

    def is_admin(self):
        return (self.roles & 4) == 4

    def is_instructor(self):
        return (self.roles & 2) == 2

    def is_ta(self):
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
        pass