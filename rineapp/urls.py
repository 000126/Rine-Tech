from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('temp', views.temp),
    path('add_new_template', views.new_template, name='add_new_template'),
    path('excel_file_list/', views.file_list, name='excl_file_list'),
    path('excel/<int:excel_id>/',
         views.view_excel, name='view_excel'),
    # path('upload/', views.upload_file, name='upload_file'),
    path('upload_word/', views.upload_word_file, name='upload_word_file'),
    path('render_word/<int:document_id>/', views.render_word_file, name='render_word_file'),
    path('list_word_files/', views.list_word_files, name='list_word_files'),

]
