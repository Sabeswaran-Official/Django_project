from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from .models import *

# Create your views here.

def LandingPage(request):

    return render(request,'home.html')

def LoginPage(request):

    context = {
        "error": ""
    }

    if request.method == "POST":

        print(request.POST)

        user = authenticate(username = request.POST['username'], password = request.POST['password'])

        

        if user is not None:

            login(request, user)
            print(f"Loggedin username:{user.username}")
        
        else:

            context = {
                "error": "*Invalid username or password"
            }

            return render(request, 'login.html', context)
        
        if request.user.is_authenticated:

            return redirect('/inventory/student_list/')

    return render(request, 'login.html', context)

def LogoutUser(request):

    logout(request)

    return redirect('/')

def SignupPage(request):

    context = {
        "error": ""
    }

    if request.method == "POST":

        user_check = User.objects.filter(username = request.POST['username'])

        if len(user_check) > 0:

            context = {
                "error": "* Username already exists!"
            }
            
            return render(request, 'signup.html', context)
        else:

            new_user = User(first_name = request.POST['fname'],last_name = request.POST['lname'],username = request.POST['username'], email = request.POST['email'])

            new_user.set_password(request.POST['password'])

            new_user.save()

            return redirect('/')

    return render(request, 'signup.html', context)