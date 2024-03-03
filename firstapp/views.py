from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.views import View
from .models import UserProfile

# Create your views here.

class Login(View):

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("base")
        else:
            messages.info(request, "Invalid username or password")
            return redirect("/")

    def get(self, request):
        return render(request, 'login.html', {'title': "Users"})
    


class Signup(View):
    def post(self, request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmPassword']
        address = request.POST['address']
        profile_picture = request.FILES.get('profilePicture')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    username=username,
                    password=password1,
                    email=email,)
                user.save()
                user_profile = UserProfile.objects.create(
                    user=user,
                    address=address,
                    profile_picture=profile_picture,
                )
                user_profile.save()
                return redirect("/")
        else:
            messages.info(request, "password not matching")
            return redirect("signup")

    def get(self, request):
        return render(request, 'signup.html')
    
class Base(View):
    def get(self, request):
        return render(request, 'base.html', {'title': "Dashboard", 'user':request.user.first_name})
    

class UserDetails(View):
    def get(self,request):
        user = request.user
        user_profile = user.userprofile
        if request.user.is_authenticated:
            return render(request, 'userdetails.html',{'title':"user",'User':user, 'user_profile': user_profile})

        return redirect("login")
    
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("login")
