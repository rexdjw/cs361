from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from main import views
from contactinfo import views as contactInfoviews

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  path("", views.Home.as_view(), name='start'),
  path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
  path('users/', include('users.urls')),
  path('users/', include('django.contrib.auth.urls')),
  path('users/allusers', views.AllUsers.as_view(), name='allUsers'),
  path('users/createaccount', views.CreateUsers.as_view(), name='createAccount'),
  path('contactInfo/', contactInfoviews.ContactInfoPage.as_view(), name='contactInfo')
]
