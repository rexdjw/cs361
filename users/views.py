# users/views.py
from django.urls import reverse_lazy
from django.views import generic, View
from django.shortcuts import render

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Account(View):
    def get(self, request):
        aUser = request.user

        auth = True
        edit = False
        return render(request, 'editMyAccount.html', {"auth": auth, "edit": edit,})

    def post(self, request):
        aUser = request.user
        username = request.POST.get("username", "")
        # = request.POST.get("password", "")


        edit = False
        aUser.reset_username(username)
        # eUser.set_password(password)
        aUser.save()
        edit = True
        return render(request, 'editMyAccount.html', { "edit": edit, "eUser": aUser})
