from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('signup', views.signup),
    path('login', views.handlelogin),
    path('logout', views.handleLogout, name="logout "),
    path('home', views.home),
    path('temp', views.temp)
]
