from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import CustomerUserCreationForms, CustomAuthenticationForm, AuthenticationForm
from django.contrib import messages

def home(request):
    # 'home.html' şablonunu render ederek kullanıcıya döndürüyoruz ve context'e request.user'ı ekliyoruz
    return render(request, 'home.html', {'user': request.user})
