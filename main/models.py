from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.db import models

# Create your models here.
from django.template.context_processors import request

from users.models import Users


class YourClass:
  # createAccount
  # deleteAccount
  # editContactInfo
  # createCourse
  # login

  def command(self, s, request):
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
        if check_password(password, user.password):
          login(request, user)
          return "Login successful!"
        else:
          return "Login failed, wrong password"
      except:
        return "Login failed, no such user"
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
          Users.create(username, password, role).save()
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
    elif cmd == "assignInstructor":
      return
    elif cmd == "removeInstructor":
      return
    elif cmd == "assignTACourse":
      return
    elif cmd == "removeTACourse":
      return
    elif cmd == "assignTALab":
      return
    elif cmd == "removeTALab":
      return
    elif cmd == "courseAssignments":
      return
    elif cmd == "readTAAssignment":
      return
    elif cmd == "readAllTAAssignment":
      return
    elif cmd == "readPublicContactInfo":
      return
    else:
      return "Unrecognized command: " + cmd

  def getActiveUser(self, request):
    if request.user.is_authenticated:
      return request.user.first_name
    else:
      return "no one logged in"
