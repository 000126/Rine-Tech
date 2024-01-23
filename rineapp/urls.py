from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('temp', views.temp),
    path('new', views.new),
    path('file_list/', views.file_list, name='file_list'),
    path('excel/<int:excel_id>/',
         views.view_excel, name='view_excel'),

]
