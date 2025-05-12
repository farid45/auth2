import uuid
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from social_django.utils import psa

# Главная страница
def index(request):
    return render(request, 'index.html')

def vk(request):
    return render(request, 'vk.html')
# Страница для начала авторизации через VK
    
# Профиль пользователя (доступ только для авторизованных пользователей)
@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
