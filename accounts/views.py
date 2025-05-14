from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')
