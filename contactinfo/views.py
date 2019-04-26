from django.shortcuts import render
from django.views import View
from users.models import Users
from contactinfo.models import ContactInfo
# Create your views here.


class ContactInfoPage(View):
    def get(self,request):
        user = Users.objects.filter(username=request.path.rsplit('/')[-2])[0]
        yourInstance = request.user
        if yourInstance.is_at_least(4) or yourInstance == user:
            return render(request, 'main/contactInfo.html', {'username': user.username, 'user': user})
        else:
            return render(request, 'publicContactInfo.html', {'username': user.username, 'user': user})


    def post(self,request):
        user = Users.objects.filter(username=request.path.rsplit('/')[-1])[0]
        nameInput = request.POST["your_name"]
        emailInput = request.POST["email"]
        officeHoursInput = request.POST["officeHours"]
        officeNumberInput = request.POST["officeNumber"]
        phoneNumberInput = request.POST["phone"]
        addressInput = request.POST["address"]

        ci = ContactInfo.objects.filter(account=user)

        if not ci.exists():
            ContactInfo.objects.create(account=user)
        if nameInput is not None:
            user.contactinfo.updateName(nameInput)
        if emailInput is not None:
            user.contactinfo.updateEmail(emailInput)
        if officeHoursInput is not None:
            user.contactinfo.updateOfficeHours(officeHoursInput)
        if officeNumberInput is not None:
            user.contactinfo.updateOfficeNumber(officeNumberInput)
        if phoneNumberInput is not None:
            user.contactinfo.updatePhoneNumber(phoneNumberInput)
        if addressInput is not None:
            user.contactinfo.updateAddress(addressInput)
        return render(request, 'main/contactInfo.html', {'username': user.username, 'user': user,
                                                         "message": "Contact Info Edited!"})

class ContactInfoPageLink(View):

    def get(self,request):
        user = Users.objects.filter(username=request.path.rsplit('/')[-2])[0]
        yourInstance = request.user
        if yourInstance.is_at_least(4) or yourInstance == user:
            return render(request, 'main/contactInfo.html', {'username': user.username, 'user': user})
        else:
            return render(request, 'publicContactInfo.html', {'username': user.username, 'user': user})


    def post(self,request):
        user = Users.objects.filter(username=request.path.rsplit('/')[-1])[0]
        yourInstance = request.user
        nameInput = request.POST["your_name"]
        emailInput = request.POST["email"]
        officeHoursInput = request.POST["officeHours"]
        officeNumberInput = request.POST["officeNumber"]
        phoneNumberInput = request.POST["phone"]
        addressInput = request.POST["address"]
        if nameInput is not None:
            user.contactinfo.updateName(nameInput)
        if emailInput is not None:
            user.contactinfo.updateEmail(emailInput)
        if officeHoursInput is not None:
            user.contactinfo.updateOfficeHours(officeHoursInput)
        if officeNumberInput is not None:
            user.contactinfo.updateOfficeNumber(officeNumberInput)
        if phoneNumberInput is not None:
            user.contactinfo.updatePhoneNumber(phoneNumberInput)
        if addressInput is not None:
            user.contactinfo.updateAddress(addressInput)
        return render(request, 'main/contactInfo.html', {'username': user.username, 'user': user},
                      {"message": "Contact Info Edited!"})