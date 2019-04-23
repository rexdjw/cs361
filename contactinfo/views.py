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
        officeNumberInput = request.POST["officeNumber"]
        phoneNumberInput = request.POST["phone"]
        addressInput = request.POST["address"]
        if(nameInput):
            yourInstance.contactinfo.updateName(nameInput)
        if(emailInput):
            yourInstance.contactinfo.updateEmail(emailInput)
        if(officeHoursInput):
            yourInstance.contactinfo.updateOfficeHours(officeHoursInput)
        if(officeNumberInput):
            yourInstance.contactinfo.updateOfficeNumber(officeNumberInput)
        if(phoneNumberInput):
            yourInstance.contactinfo.updatePhoneNumber(phoneNumberInput)
        if(addressInput):
            yourInstance.contactinfo.updateAddress(addressInput)
        return render(request, 'main/contactInfo.html')


class OtherContactInfoPage(View):
    def get(self, request):
        return render(request, 'main/contactInfo.html')

    def post(self, request):
        yourInstance = ContactInfo()
        nameInput = request.POST["your_name"]
        if nameInput:
            yourInstance.updateName(request.username, nameInput)
        return render(request, 'main/contactInfo.html')