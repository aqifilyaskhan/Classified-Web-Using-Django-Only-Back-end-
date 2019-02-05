from django.contrib.auth.models import User
from django.db import models

class Profiles(models.Model):
	# p2=  models.CharField(max_length=14)
	phone = models.CharField(max_length=14)
	city = models.CharField(max_length=20)
	province = models.CharField(max_length=20)
	username2 = models.ForeignKey(User, on_delete=models.CASCADE)