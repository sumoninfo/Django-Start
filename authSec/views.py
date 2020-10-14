from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def authLogin(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Your Email & password Invalid!')
    return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already Exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already Exist')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Register Successfully, please login now')
                return redirect('login')
        else:
            messages.error(request, 'Your Password & Confirm password Not matched!')

    #     user = authenticate(request, username=user_name, password=password)
    # if user is not None:
    #     login(request, user)
    #     messages.success(request, 'Register Successfully')
    #     return redirect('profile')
    # else:
    #     messages.error(request, 'Your Email & password Invalid!')

    return render(request, 'auth/register.html')


def forgotPassword(request):
    return render(request, 'auth/forgotPassword.html')


def authLogout(request):
    logout(request)
    return redirect('login')
