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
  all = Users.objects.all()
  def get(self, request):
    return render(request, 'allusers.html', {"all" : self.all})
  def post(self, request):
    return render(request, 'allusers.html', {"all" : self.all})
