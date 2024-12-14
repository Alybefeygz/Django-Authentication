from django.urls import path
from .views import register, login_view, profile, logout_view, home

urlpatterns = [
    path('',home, name = 'home'),
    path('register/', register, name= 'register'),
    path('login/', login_view, name= 'login'),
    path('profile/', profile, name= 'profile'),
    path('logout/', logout_view, name= 'logout'),

    
]
