from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserChangeForm, CustomerUserCreationForms, CustomAuthenticationForm, AuthenticationForm
from django.contrib import messages

def home(request):
    # 'home.html' şablonunu render ederek kullanıcıya döndürüyoruz ve context'e request.user'ı ekliyoruz
    return render(request, 'home.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = CustomerUserCreationForms()
    return render(request,'user/register.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
        
    return render(request,'user/login.html',{'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile wa succesfully updated!')
            return redirect('profile')
        else:
            form = CustomUserChangeForm(instance=request.user)
        return render(request, 'user/profile.html')
    
def logout_view(request):
    logout(request)
    messages.info(request,'You have been logged out')
    return redirect('home')