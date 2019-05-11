from django.shortcuts import render
from django.views import View
from lab.models import Lab
from course.models import Course
from users.models import Users
from ta.models import TA
# Create your views here.


class CreateLabPage(View):
    def get(self, request):
        current_user = request.user
        permission_check = current_user.is_at_least(4)
        courseInfo = request.path.rsplit('/')[-1]
        course = Course.objects.filter(courseName=courseInfo).first()
        auth = True
        create = False
        return render(request, 'createLab.html',
                      {"permission_check": permission_check, "auth": auth, "create": create, "courseInfo": courseInfo, "course" : course})

    def post(self, request):
        current_user = request.user
        labNumber = request.POST.get("Lab Number", "")
        TAs = request.POST.get("TAs", "")
        courseInfo = request.path.rsplit('/')[-1]
        course = Course.objects.filter(courseName=courseInfo).first()
        # add functionality to assign instructor upon creation

        permission_check = current_user.is_at_least(4)

        lab_already_exists = Lab.objects.filter(labNumber=labNumber)
        create = False

        if((current_user.roles != 8) and (course.instructor != current_user)):
            return render(request, 'createLab.html',
                          {"permission_check": permission_check, "courseInfo": courseInfo, "course": course,
                           "create": create, "message": "Error! Only Surpervisors or Instructor " + course.instructor.username + " can make labs and assign TAS"})

        elif permission_check and not lab_already_exists:
            create = True
            courseToAdd = Course.objects.filter(courseName=courseInfo)
            course = courseToAdd.first()
            course.create_lab_section(labNumber)

            if TAs is None:
                TAToAdd = Users.objects.filter(username=TAs)
                TAToFind = TAToAdd.first()
                createTA = TA.objects.filter(account=TAToFind)
                labSection = Lab.objects.filter(labNumber=labNumber)
                lab = labSection.first()
                lab.assign_TA(createTA.first())

            return render(request, 'createLab.html', {"permission_check": permission_check, "course" : course, "create" : create, "courseInfo": courseInfo})
        else:
            return render(request, 'createLab.html',
                          {"permission_check": permission_check, "courseInfo": courseInfo, "course" : course, "create": create, "message": "Error! The lab "
                                                                                              + labNumber + " " + " already exists"})


