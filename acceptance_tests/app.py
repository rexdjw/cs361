class App:
    # createAccount
    # deleteAccount
    # editContactInfo
    # createCourse
    # login

    def command(self, s):
        tokens = s.split
        cmd = tokens[0]
        args = tokens[1:]
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
            # todo : check permissions
            # todo : call create course
            return
        elif cmd == "createAccount":
            if len(args) < 3:
                return "Insufficient arguments for command " + cmd
            username = args[0]
            password = args[1]
            role = int(args[2])
            # todo : check permissions
            # todo : call create account
            return
        elif cmd == "deleteAccount":
            if len(args) < 1:
                return "Insufficient arguments for command " + cmd
            username = args[0]
            # todo : check permissions
            # todo : call delete account
            return
        elif cmd == "editContactInfo":
            # todo
            return
        # todo : support other commands
        else:
            return "Unrecognized command: " + cmd
        pass