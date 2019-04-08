from ..users.models import Users


class App:
    # createAccount
    # deleteAccount
    # editContactInfo
    # createCourse
    # login

    def command(self, s):
        tokens = s.split
        cmd = tokens.head
        args = tokens.tail
        if cmd == "login":
            if len(args) < 2:
                return "Insufficient arguments for command " + cmd
            username = args[0]
            password = args[1]
            # todo : call login
            return
        elif cmd == "createCourse":
            if len(args) < 3:
                return "Insufficient arguments for command " + cmd
            coursename = args[0]
            department = args[1]
            coursenumber = args[2]
            permission = True  # todo : check permissions of active user
            # todo : call create course
            return
        elif cmd == "createAccount":
            if len(args) < 3:
                return "Insufficient arguments for command " + cmd
            username = args[0]
            password = args[1]
            role = int(args[2])
            permission = True  # todo : check active user is_admin
            greater = True  # todo : check that active user is_above(role)
            exists = False  # todo : query the database to find out if the active user exists
            if permission:
                if exists:
                    return "Account " + username + " already exists!"
                elif not greater:
                    return "Permission denied - Cannot create account with that role!"
                else:
                    Users.create(username, password, role)
                    return "Account " + username + " created successfully."
            else:
                return "Permission denied - Your role may not create accounts!"
        elif cmd == "deleteAccount":
            if len(args) < 1:
                return "Insufficient arguments for command " + cmd
            username = args[0]
            permission = True  # todo : check permissions of active user
            exists = True  # todo : query the database to find out if the active user exists
            # todo : call delete account
            return
        elif cmd == "editContactInfo":
            # todo
            return
        # todo : support other commands
        else:
            return "Unrecognized command: " + cmd