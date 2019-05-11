from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

from course.views import ViewCourse, AssignInstructor, AssignTA
from main import views as mainViews
from contactinfo import views as contactInfoviews
from course import views as CourseViews
from lab import views as LabViews
from users import views as UserViews
from django.contrib.auth import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  path("", mainViews.Home.as_view(), name='start'),
  path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
  path('users/', include('users.urls')),
  path('users/', include('django.contrib.auth.urls')),
  path('users/allusers', mainViews.AllUsers.as_view(), name='allUsers'),
  path('users/createaccount', mainViews.CreateUsers.as_view(), name='createAccount'),
  path('users/courses', CourseViews.AllCourses.as_view(), name='AllCourses'),
  path('users/createCourse', CourseViews.CreateCourse.as_view(), name = 'createCourse'),
  re_path(r'contactInfo/', contactInfoviews.ContactInfoPage.as_view(), name='contactInfo'),
  re_path(r'users/editaccount', mainViews.EditUsers.as_view(), name='editAccount'),
  re_path(r'users/editMyAccount', UserViews.Account.as_view(), name='editMyAccount'),
  re_path(r'users/deleteaccount', mainViews.DeleteUsers.as_view(), name='deleteAccount'),
  url(r'^courses/(?P<course>[a-zA-Z0-9]+)', ViewCourse.as_view(), name="course"),
  re_path(r'createLab/', LabViews.CreateLabPage.as_view(), name='createLab'),
  url(r'^assignInstructor/(?P<course>[a-zA-Z0-9]+)', AssignInstructor.as_view(), name="course"),
  url(r'^assignTA/(?P<course>[a-zA-Z0-9]+)', AssignTA.as_view(), name="course"),
  url('^', include('django.contrib.auth.urls')),
  path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
  path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
