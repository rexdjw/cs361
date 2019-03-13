class Users:

    def __init__(self, username=None, password=None, roles=None, contact_info=None):
        self.username = username
        self.password = password
        self.roles = roles
        self.contact_info = contact_info

    def createAccount(self, username, password, roles):
        pass

    def deleteAccount(self, username):
        pass

    def editAccountInfo(self, username, new_username, password, account_roles):
        pass

    def getRoles(self):
        pass

    def isAtLeast(self, role):
        pass

    def displayUsers(self):
        pass

    def displayUsersByRole(self, role):
        pass

    def displayUserAssignments(self, role):
        pass

    def editAccountInfo(self, username, new_username, password, roles):
        pass

    def dispose(self):
        pass