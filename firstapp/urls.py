from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path("", views.Login.as_view(), name='login'),
    path("signup", views.Signup.as_view(), name='signup'),
    path("user", views.UserDetails.as_view(), name='user'),
    path("base", views.Base.as_view(), name='base'),
    path("logout",views.Logout.as_view(),name='logout'),
   
]