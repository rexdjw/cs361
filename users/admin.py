from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users


# TODO: Override User Admin
admin.site.register(Users, UserAdmin)
