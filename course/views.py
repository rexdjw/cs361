from django.shortcuts import render
from django.views import View
from course.models import Course

class AllCourses(View):
  def get(self, request):
    self.all = Course.objects.all()

    return render(request, 'allCourses.html', {"all" : self.all})
  def post(self, request):
    return render(request, 'allCourses.html', {"all" : self.all})




class CreateCourse(View):
  def get(self, request):
    current_user = request.user
    permission_check = current_user.is_at_least(4)
    auth = True
    create = False
    return render(request, 'createCourse.html', {"permission_check": permission_check, "auth" : auth, "create" : create})

  def post(self, request):
    current_user = request.user
    course_name = request.POST.get("Course Name", "")
    department = request.POST.get("Department", "")
    course_number = int(request.POST.get("Course Number", ""))
    # add functionality to assign instructor upon creation

    permission_check = current_user.is_at_least(4)

    course_name_already_exists = Course.objects.filter(courseName=course_name)
    course_number_already_exists = Course.objects.filter(courseNumber=course_number)
    create = False

    if permission_check and not course_name_already_exists and not course_number_already_exists:
        new_course = Course.create(course_name,department,course_number)
        new_course.save()
        create = True
        return render(request, 'createCourse.html', {"permission_check": permission_check, "create" : create})
    else:
      return render(request, 'createCourse.html', {"permission_check": permission_check, "create" : create, "message" : "Error! The course "
                                                   + course_name + " " + course_number.__str__() + " already exists"})