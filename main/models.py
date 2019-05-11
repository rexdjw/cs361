from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.db import models

# Create your models here.
from django.template.context_processors import request

from contactinfo.models import ContactInfo
from course.models import Course
from lab.models import Lab
from ta.models import TA
from users.models import Users


class YourClass:
  # createAccount
  # deleteAccount
  # editContactInfo
  # createCourse
  # login

  def command(self, s, request):
    try:
      currentUser = self.getActiveUser(request)
    except:
      pass
    tokens = s.split()
    cmd = tokens[0]
    args = tokens[1:]
    if cmd == "login":
      if len(args) < 2:
        return "Insufficient arguments for command " + cmd
      username = args[0]
      password = args[1]
      try:
        user = Users.objects.get(username=username)
        if user.check_password(password):
          login(request, user)
          return "Login successful."
        else:
          return "Login failed, wrong password"
      except Exception as e:
        print(e)
        return "Login failed, no such user"
    elif cmd == 'logout':
      logout(request)
      return "Logged out"
    elif cmd == "createCourse":
      return "Pass - implemented in Web Interface not Command Line."
      if len(args) < 3:
        return "Insufficient arguments for command " + cmd
      coursename = args[0]
      department = args[1]
      coursenumber = args[2]
      permission = True  # todo : check permissions of active user
      Course.create(coursename, department, coursenumber).save()
      return "Course created successfully."
    elif cmd == "createAccount":
      if len(args) < 3:
        return "Insufficient arguments for command " + cmd
      username = args[0]
      password = args[1]
      role = int(args[2])
      try:
        permission = self.getActiveUser(request).is_at_least(4)
      except:
        return "Permission denied - Your role may not create accounts!"
      greater = self.getActiveUser(request).is_at_least(role)
      if permission:
        if not greater:
          return "Permission denied - Your role may not create accounts of this type!"
        else:
          try:
            user = Users.create(username, password, role)
            user.set_password(password) #hashing fix
            user.save() #ci looks for user in db so save first
            user.set_contact_info("","","","","","") #initialize ci
            user.save() #now save updated ci
          except:
            return "Account already exists!"
          return "Account created successfully."
      else:
        return "Permission denied - Your role may not create accounts!"
    elif cmd == "deleteAccount":
      if len(args) < 1:
        return "Insufficient arguments for command " + cmd
      username = args[0]
      permission = self.getActiveUser(request).is_at_least(4)
      user = Users.objects.filter(username=username)
      if len(user) == 0:
        return "No such user"
      if not self.getActiveUser(request).is_at_least(user[0].roles):
        return "Permission denied - Your role may not delete accounts of this type!"
      user[0].delete()
      return "User deleted"
    elif cmd == "editContactInfo":
      if len(args) < 6:
        return "Missing arguments"
      if len(args) > 6:
        return "Field does not exist"
      try:
        u = self.getActiveUser(request)
        if not u:
          return "Login a user first"
        if len(ContactInfo.objects.filter(account=u)) == 0:
          ContactInfo.create(u.username, args[0], args[1], args[2], args[3], args[4], args[5]).save()
          return "field successfully revised"
        u.editContactInfo(u, args[0], args[1], args[2], args[3], args[4], args[5])
        return "field successfully revised"
      except:
        return "Login a user first"
    # todo : support other commands
    elif cmd == "assignInstructor":
      return "Pass - implemented in Web Interface not Command Line."
      course = Course.objects.get(courseName=args[0])
      user = Users.objects.get(username=args[1])
      course.assign_instructor(user)
      return "Successfully added instructor to course"
    elif cmd == "removeInstructor":
      return "Pass - implemented in Web Interface not Command Line."
    elif cmd == "assignTACourse":
      return "Pass - implemented in Web Interface not Command Line."
      course = Course.objects.get(courseName=args[0])
      user = Users.objects.get(username=args[1])
      ta = TA.create(user, True, 1)
      ta.save()
      course.assign_TA(ta)
      return "Successfully added TA to course"
    elif cmd == "sendEmail":
      return "Failed- Unimplemented"
    elif cmd == "removeTACourse":
      return "Pass - implemented in Web Interface not Command Line."
      return
    elif cmd == "assignTALab":
      return "Pass - implemented in Web Interface not Command Line."
      lab = Lab.objects.get(labNumber=args[0])
      user = Users.objects.get(username=args[1])
      ta = TA.create(user, True, 1)
      ta.save()
      lab.assign_TA(ta)
      return "Successfully added TA to lab"
    elif cmd == "removeTALab":
      return "Pass - implemented in Web Interface not Command Line."
      return
    elif cmd == "courseAssignments":
      return "Pass - implemented in Web Interface not Command Line."
      return
    elif cmd == "readTAAssignment":
      return "Pass - implemented in Web Interface not Command Line."
      return
    elif cmd == "readAllTAAssignment":
      return "Pass - implemented in Web Interface not Command Line."
      return
    elif cmd == "readPublicContactInfo":
      return "Pass - implemented in Web Interface not Command Line."
    elif cmd == "readAllTAAssignments":
      return "Pass - implemented in Web Interface not Command Line."
    elif cmd == "editAccount":
      return "Pass - implemented in Web Interface not Command Line."
    else:
      return "Unrecognized command: " + cmd

  def getActiveUser(self, request):
    if request.user.is_authenticated:
      return request.user
    else:
      return "no one logged in"
