from django.contrib.auth.models import User
from django.db import models

	# cat = models.IntegerField(max_length=5)

class Post(models.Model):
	title = models.CharField(max_length=75)
	description = models.TextField()
	price = models.CharField(max_length=5)
	phone = models.CharField(max_length=13)
	cat = models.CharField(max_length=5)
	image = models.ImageField(upload_to='images/')
	city = models.CharField(max_length=20)
	province = models.CharField(max_length=20)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField()
