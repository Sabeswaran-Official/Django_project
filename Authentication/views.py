from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def LandingPage(request):

    return render(request,'home.html')

def LoginPage(request):
    if request.user.is_authenticated:

        return redirect('/inventory/students_detail/')

    context = {
        "error": ""
    }

    if request.method == "POST":

        print(request.POST)

        user = authenticate(username = request.POST['username'], password = request.POST['password'])

        

        if user is not None:

            login(request, user)
  
        
        else:

            context = {
                "error": "*Invalid username or password"
            }

            return render(request, 'login.html', context)

    return render(request, 'login.html', context)

def LogoutUser(request):

    logout(request)

    return redirect('')
    return render(request,'home.html')

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

            new_user = User(full_name = request.POST['name'],username = request.POST['username'], reg_no = request.POST['reg_no'], course = request.POST['course'], year = request.POST['year'], gpa = request.POST['gpa'], gmail_id = request.POST['email'], photo = request.POST['profile_photo'])

            new_user.set_password(request.POST['password'])

            new_user.save()

            return redirect('/')

    return render(request, 'signup.html', context)