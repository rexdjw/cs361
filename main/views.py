from django.shortcuts import render
from django.views import View
from main.models import YourClass
from users.models import Users
# Create your views here.
class Home(View):
  def get(self,request):
    return render(request, 'main/index.html')
  def post(self,request):
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
    create = False
    if ok and auth:
        user = Users.create(username, password, roles)
        user.set_password(password)
        user.save()
        create = True
    return render(request, 'createaccount.html', {"ok" : ok, "auth" : auth, "create" : create})
