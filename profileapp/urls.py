from typing import ValuesView
from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.login_user, name = 'login'),
    path('register/', views.register_user, name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
]