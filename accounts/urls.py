from django.urls import path

from .import views

urlpatterns = [
    path('', views.account, name='account'),
    path('account/', views.account, name='account'),
    path('signup/', views.signup, name='signup'),
    path('signup-next/', views.signup2, name='signup2'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
