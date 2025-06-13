from django.contrib import admin 
from django.urls import path ,include

from .views import *


urlpatterns = [
    path('',LandingPage),
    path('login/',LoginPage),
    path('signup/',SignupPage),
    path('logout/',LogoutUser),
    
    
]
