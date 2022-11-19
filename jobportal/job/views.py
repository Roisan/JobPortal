from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def admin_login(request):
    return render(request, 'admin_login.html')


def user_login(request):
    return render(request, 'user_login.html')


def recruiter_login(request):
    return render(request, 'recruiter_login.html')


def user_signup(request):
    return render(request, 'user_signup.html')


