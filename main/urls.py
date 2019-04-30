from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from main import views
from contactinfo import views as contactInfoviews
from course import views as CourseViews

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  path("", views.Home.as_view(), name='start'),
  path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
  path('users/', include('users.urls')),
  path('users/', include('django.contrib.auth.urls')),
  path('users/allusers', views.AllUsers.as_view(), name='allUsers'),
  path('users/createaccount', views.CreateUsers.as_view(), name='createAccount'),
  path('users/courses', CourseViews.AllCourses.as_view(), name='AllCourses'),
  path('users/createCourse', CourseViews.CreateCourse.as_view(), name = 'createCourse'),
  re_path(r'contactInfo/', contactInfoviews.ContactInfoPage.as_view(), name='contactInfo'),
  re_path(r'users/editaccount', views.EditUsers.as_view(), name='editAccount'),
]
