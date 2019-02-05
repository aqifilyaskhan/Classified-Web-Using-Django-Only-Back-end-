from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from .import views

urlpatterns = [
    path('<int:post_id>/', views.detail, name='detail'),
    path('pending/<int:post_id>/', views.pending, name='pending'),
    path('city/<slug:post_city>/', views.city, name='city'),
    path('create/', views.create, name='create'),
    path('listing/<int:post_cat>/', views.listing, name='listing'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

