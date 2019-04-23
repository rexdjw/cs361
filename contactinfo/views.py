from django.shortcuts import render
from django.views import View
from contactinfo.models import ContactInfo
from main.models import YourClass
# Create your views here.


class ContactInfoPage(View):
    def get(self,request):
        return render(request, 'main/contactInfo.html')

    def post(self,request):
        yourInstance = ContactInfo()
        nameInput = request.POST["your_name"]
        if(nameInput):
            yourInstance.updateName(request.username, nameInput)
        return render(request, 'main/contactInfo.html')