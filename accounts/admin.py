from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profiles
admin.site.register(Profiles) 


# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ('username2','phone','city','province')

# admin.site.register(Profile,ProfileAdmin) 
