from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profiles


def account(request):
	return render(request, 'accounts/account.html')


def signup(request):
		if request.method == 'POST':
			if request.POST['password1'] == request.POST['password2']:
				try: 
					user = User.objects.get(username=request.POST['username'])
					return render(request, 'accounts/signup.html', {'issue':'username is already taken'})
				except User.DoesNotExist:
					user = User.objects.create_user(request.POST['username'], password=request.POST['password1'],email=request.POST['email'],first_name=request.POST['fname'],last_name=request.POST['lname'])
					auth.login(request, user)
					return redirect(signup2)
			else:
				return render(request, 'accounts/signup.html', {'issue':'password not matching'})
		else:
			return render(request, 'accounts/signup.html')

def signup2(request):
	if request.method == 'POST':
		more_info = Profiles()
		more_info.phone = request.POST['phone']
		more_info.city = request.POST['city'] 
		more_info.province = request.POST['province'] 
		more_info.username2 = request.user
		more_info.save()
		return redirect('/ads/create')

	else:
		return render(request, "accounts/signup-verification.html")

def login(request):
	if request.method=='POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('/ads/create')
		else:
			return render(request, 'accounts/login.html')
	else:
		return render(request, 'accounts/login.html')

def logout(request):
	if request.method=='POST':
		auth.logout(request)
		return redirect(signup)