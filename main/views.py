from django.shortcuts import render
from django.views import View
from main.models import YourClass
from users.models import Users
from course.models import Course
from contactinfo.models import ContactInfo
# Create your views here.


class Home(View):
  def get(self, request):
    return render(request, 'main/index.html')
  def post(self, request):
    yourInstance = YourClass()
    commandInput = request.POST["command"]
    if commandInput:
      response = yourInstance.command(commandInput, request)
    else:
      response = ""
    return render(request, 'main/index.html',{"message":response})

class AllUsers(View):
  def getKey(self, user):
    return user.roles
  def get(self, request):
    users = Users.objects.all()
    self.all = sorted(users, key=self.getKey, reverse=True)
    return render(request, 'allusers.html', {"all" : self.all})
  def post(self, request):
    return render(request, 'allusers.html', {"all" : self.all})

class CreateUsers(View):
  def get(self, request):
    aUser = request.user
    ok = aUser.is_at_least(4)
    auth = True
    create = False
    return render(request, 'createaccount.html', {"ok" : ok, "auth" : auth, "create" : create})

  def post(self, request):
    aUser = request.user
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    roles = int(request.POST.get("roles", ""))
    ok = aUser.is_at_least(4)
    auth = aUser.is_at_least(roles) and roles < 8 #cannot create multiple supervisors
                                                  # why not??? - Sean

    alreadyCreated = Users.objects.filter(username=username)

    create = False
    if ok and auth and not alreadyCreated:
        user = Users.create(username, password, roles)
        user.set_password(password)
        user.save()
        ContactInfo.objects.create(account=user)
        create = True
        return render(request, 'createaccount.html', {"ok" : ok, "auth" : auth, "create" : create})
    else:
      return render(request, 'createaccount.html', {"ok" : ok, "auth" : auth, "create" : create,
                                                    "message": "Error! Account already exists!"})


class CreateCourse(View):
  def get(self, request):
    current_user = request.user
    permission_check = current_user.is_at_least(4)
    auth = True
    create = False
    return render(request, 'createCourse.html', {"permission_check": permission_check, "auth" : auth, "create" : create})

  def post(self, request):
    current_user = request.user
    course_name = request.POST.get("Course Name", "")
    department = request.POST.get("Department", "")
    course_number = int(request.POST.get("Course Number", ""))
    # add functionality to assign instructor upon creation

    permission_check = current_user.is_at_least(4)

    course_name_already_exists = Course.objects.filter(courseName=course_name)
    course_number_already_exists = Course.objects.filter(courseNumber=course_number)
    create = False

    if permission_check and not course_name_already_exists and not course_number_already_exists:
        new_course = Course.create(course_name,department,course_number)
        new_course.save()
        create = True
        return render(request, 'createCourse.html', {"permission_check": permission_check, "create" : create})
    else:
      return render(request, 'createCourse.html', {"permission_check": permission_check, "create" : create, "message" : "Error! The course "
                                                   + course_name + " " + course_number.__str__() + " already exists"})


