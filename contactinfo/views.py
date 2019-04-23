from django.shortcuts import render
from django.views import View
from contactinfo.models import ContactInfo
from main.models import YourClass
# Create your views here.


class ContactInfoPage(View):
    def get(self,request):
        return render(request, 'main/contactInfo.html')

    def post(self,request):

        yourInstance = request.user
        nameInput = request.POST["your_name"]
        emailInput = request.POST["email"]
        officeHoursInput = request.POST["officeHours"]
        if(nameInput):
            yourInstance.contactinfo.updateName(nameInput)
        if(emailInput):
            yourInstance.contactinfo.updateEmail(emailInput)
        if(officeHoursInput):
            yourInstance.contactinfo.updateOfficeHours(officeHoursInput)
        return render(request, 'main/contactInfo.html')