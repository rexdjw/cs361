from django.shortcuts import render
from django.views import View
from main.models import YourClass
from users.models import Users
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
    edit = request.user.is_at_least(4)
    users = Users.objects.all()
    self.all = sorted(users, key=self.getKey, reverse=True)
    return render(request, 'allusers.html', {"all" : self.all, "edit" : edit})
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
    auth = aUser.is_at_least(roles)

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
class EditUsers(View):
  def get(self, request):
    aUser = request.user
    eUser = Users.objects.filter(username=request.path.rsplit('/')[-1])[0]
    ok = aUser.is_at_least(4)
    auth = True
    edit = False
    return render(request, 'editaccount.html', {"ok" : ok, "auth" : auth, "edit" : edit, "eUser" : eUser})

  def post(self, request):
    aUser = request.user
    eUser = Users.objects.filter(username=request.path.rsplit('/')[-1])[0]
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    roles = int(request.POST.get("roles", ""))
    ok = aUser.is_at_least(4)
    auth = aUser.is_above(eUser.roles) and aUser.is_above(roles)

    edit = False
    if ok and auth:
        eUser.reset_username(username)
        eUser.set_password(password)
        eUser.reset_roles(roles)
        eUser.save()
        edit = True
    return render(request, 'editaccount.html', {"ok": ok, "auth": auth, "edit" : edit, "eUser": eUser})


