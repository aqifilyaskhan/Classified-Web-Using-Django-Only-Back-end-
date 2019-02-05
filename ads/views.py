# from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone 

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Post

def detail(request, post_id):
    detail =  get_object_or_404(Post, pk=post_id)
    return render(request, 'ads/detail.html',{'detail':detail})


def pending(request, post_id):
    pending =  get_object_or_404(Post, pk=post_id)
    return render(request, 'ads/pending.html',{'detail':pending})


# @login_required
def create(request):
    if request.method =="POST":
        more_info = Post()
        more_info.title = request.POST['title']
        more_info.description = request.POST['description']
        more_info.cat = request.POST['cat']
        more_info.phone = request.POST['phone']
        more_info.image = request.FILES['image']
        more_info.price = request.POST['price']
        more_info.city = request.POST['city'] 
        more_info.province = request.POST['province'] 
        more_info.pub_date = timezone.datetime.now() 
        more_info.username = request.user
        more_info.save()
        return redirect('/ads/pending/'+str(more_info.id))
        # return redirect('/detail/'+str(product.id))
    else:
        return render(request, 'ads/create.html')


# def listing(request):
#     user_list = Post.objects.all()
#     paginator = Paginator(user_list, 5) #kitna data per page
#     page = request.GET.get('page') #url iske through page object le raha hai
#     # page = request.GET.get('page', 2) #ye url k liye page

#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)

#     return render(request, 'ads/listing.html', { 'users': users })


def listing(request,post_cat):
    var_cat =  Post.objects.filter(cat=post_cat)    
    paginator = Paginator(var_cat, 5)
    page = request.GET.get('page') 

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
            users = paginator.page(1)
    except EmptyPage:
            users = paginator.page(paginator.num_pages)

    return render(request, 'ads/listing.html', { 'users': users })


def city(request,post_city):
    var_cat =  Post.objects.filter(city=post_city)    
    paginator = Paginator(var_cat, 5)
    page = request.GET.get('page') 

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
            users = paginator.page(1)
    except EmptyPage:
            users = paginator.page(paginator.num_pages)

    return render(request, 'ads/city.html', { 'users': users })

