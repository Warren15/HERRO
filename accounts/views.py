from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth import get_user_model,login,logout,authenticate

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        gym = request.POST.get("gym")
        
        user = User.objects.create_user(username = username,
                                        password = password,
                                        gym = gym)
        login(request,user)
        return redirect("index")
    return render(request,"accounts\signup.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        gym = request.POST.get("gym")
        
        user = authenticate(username=username,
                           password=password,
                           gym = gym)
        if user:
            login(request,user)
            return redirect("index")
    return render(request, "accounts/login.html")

def logout_user(request):
    logout(request)
    return redirect("index")