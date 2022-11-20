from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, 'index.html')


def admin_login(request):
    return render(request, 'admin_login.html')



def user_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = JobSeeker.objects.get(user=user)
                if user1.type == "jobseeker":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"

    d = {'error': error}
    return render(request, 'user_login.html', d)


def recruiter_login(request):
    return render(request, 'recruiter_login.html')


def user_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            JobSeeker.objects.create(user=user, mobile=con, image=i, gender=gen, type="jobseeker")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'user_signup.html', d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user_home.html')
