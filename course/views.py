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

class ViewCourse(View):
  def get(self, request, **kwargs):
    current_user = request.user

    coursename = self.kwargs["course"] if "course" in self.kwargs else request.session["course"]
    course = Course.objects.filter(courseName=coursename)[0]

    return render(request, "course.html", {"course": course})


class AssignInstructor(View):
  def get(self, request, **kwargs):
    current_user = request.user
    coursename = self.kwargs["course"] if "course" in self.kwargs else request.session["course"]
    course = Course.objects.filter(courseName=coursename)[0]
    permission_check = current_user.is_at_least(4)
    from users.models import Users
    instructors = Users.objects.filter(roles__gte=2).exclude(username=course.instructor.username)

    return render(request, "assignInstructor.html", {"course": course, "permission_check": permission_check, "instructors": instructors})

  def post(self, request, **kwargs):
    from users.models import Users
    current_user = request.user
    coursename = self.kwargs["course"] if "course" in self.kwargs else request.session["course"]
    instructor = request.POST.get("Instructors", "")
    if instructor:
      usr = Users.objects.filter(username=instructor)[0]
    course = Course.objects.filter(courseName=coursename)[0]
    permission_check = current_user.is_at_least(4)

    course.assign_instructor(usr)


    instructors = Users.objects.filter(roles__gte=2).exclude(username=instructor)

    return render(request, "assignInstructor.html",
                  {"course": course, "permission_check": permission_check, "instructors": instructors, "create": True})


class AssignTA(View):
  def get(self, request, **kwargs):
    current_user = request.user
    coursename = self.kwargs["course"] if "course" in self.kwargs else request.session["course"]
    course = Course.objects.filter(courseName=coursename)[0]
    permission_check = current_user.is_at_least(2)
    from users.models import Users

    tas = Users.objects.filter(roles__gte=1).exclude(username__in=[x for x in course.TAs.all()])

    return render(request, "assignTA.html", {"course": course, "permission_check": permission_check, "tas": tas})

  def post(self, request, **kwargs):
    from users.models import Users
    current_user = request.user
    coursename = self.kwargs["course"] if "course" in self.kwargs else request.session["course"]
    ta = request.POST.get("TAs", "")
    if ta:
      usr = Users.objects.filter(username=ta)[0]
    course = Course.objects.filter(courseName=coursename)[0]
    permission_check = current_user.is_at_least(2)

    from ta.models import TA
    try:
      tmp = TA.objects.filter(account=usr)[0]
    except:
      tmp = TA.create(usr)
      tmp.graderStatus = True
      tmp.numberOfLabs = 1
      tmp.save()

    course.assign_TA(tmp)


    tas = Users.objects.filter(roles__gte=2).exclude(username__in=[x for x in course.TAs.all()])

    return render(request, "assignTA.html",
                  {"course": course, "permission_check": permission_check, "tas": tas, "create": True})