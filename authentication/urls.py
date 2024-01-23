from django.urls import path
from .views import *
urlpatterns = [

    path('signup/', signup, name='signup'),
    path('login/', sys_login, name='login'),
    path('logout/', handleLogout, name="logout "),
    path('user-list/', user_list, name='user_list'),
]
