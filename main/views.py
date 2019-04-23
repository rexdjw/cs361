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
  users = Users.objects.all()
  def getKey(user):
    return user.roles
  all = sorted(users, key=getKey, reverse=True)
  def get(self, request):
    return render(request, 'allusers.html', {"all" : self.all})
  def post(self, request):
    return render(request, 'allusers.html', {"all" : self.all})

class CreateUsers(View):
  def get(self, request):
    aUser = request.user
    ok = aUser.is_at_least(4)
    return render(request, 'createaccount.html', {"ok" : ok})
  def post(self, request):
    aUser = request.user
    ok = aUser.is_at_least(4)
    return render(request, 'createaccount.html', {"ok" : ok})
