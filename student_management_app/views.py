from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from student_management_app.EmailBackEnd import EmailBackEnd


def home(request):
    return render(request, 'index.html')


def loginPage(request):
    return render(request, 'login.html')


def signupUser(request):
    return render(request,"signup.html")


def signup_process(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    email=request.POST.get("email")
    first_name=request.POST.get("first_name")
    last_name=request.POST.get("last_name")

    if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
        user=User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        messages.success(request,"Signup Successfull")
    else:
        messages.error(request,"Username or Email Already Exist")
    
    return HttpResponseRedirect(reverse("signup"))


def login_proces(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    user=authenticate(username=username,password=password)

    if user!=None:
        login(request,user)
        #messages.success(request,"Login Successfull")
        return HttpResponseRedirect(reverse("home"))
    else:
        messages.error(request,"Invalid Login Details")
        return HttpResponseRedirect(reverse("login"))


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
                
            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')



def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


