from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
# from .forms import RegistrationForm
from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import *
from django.contrib.auth import authenticate, login, logout

import pandas as pd
from .models import ExcelDocument
from django.contrib.auth import get_user_model
User = get_user_model()


def index(request):
    return render(request, 'index.html')


# def signup(request):
#     if request.method == "POST":
#         user_type = request.POST.get('user_type')
#         username = request.POST.get('usernumber')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')

#         if len(username) > 10 or len(username) < 10:
#             messages.info(request, "Phone Number Must be 10 Digits")
#             return redirect('/signup')

#         if pass1 != pass2:
#             messages.info(request, "Password is not Matching")
#             return redirect('/signup')

#         try:
#             if User.objects.get(username=username):
#                 messages.warning(request, "Phone Number is Taken")
#                 return redirect('/signup')

#         except Exception as identifier:
#             pass

#         try:
#             if User.objects.get(email=email):
#                 messages.warning(request, "Email is Taken")
#                 return redirect('/signup')

#         except Exception as identifier:
#             pass

#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.save()
#         messages.success(request, "User is Created Please Login")
#         return redirect('/login')

#     return render(request, "signup.html")


# def handlelogin(request):
#     if request.method == "POST":
#         username = request.POST.get('usernumber')
#         pass1 = request.POST.get('pass1')
#         myuser = authenticate(username=username, password=pass1)
#         if myuser is not None:
#             login(request, myuser)
#             messages.success(request, "Login Successful")
#             return redirect('/home')
#         else:
#             messages.error(request, "Invalid Credentials")
#             return redirect('/login')

#     return render(request, "login.html")


def home(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login and Try Again")
        return redirect('/login')
    # Template = Template.objects.all()
    # if request.method == 'POST':
    #     temp_na = request.POST.get('template_name')
    #     temp_type = request.POST.get('template_type')
    #     p_code = request.POST.get('P_code')
    #     batch_num = request.POST.get('batch_num')
    #     a_r = request.POST.get('a_r number')
    #     Template = Template.objects.filter(
    #         template=temp_na, template_type=temp_type, project_code=p_code, batch_no=batch_num, a_r_no=a_r)
    # context = {
    #     'Temp': Template
    # }
    return render(request, "home.html",)


def temp(request):
    return render(request, "awc.html")


# def your_view(request):
#     result = ExcelFormulaApp()
#     return render(request, 'template_name.html', {'result': result})


@csrf_exempt
def get_data(request):
    # Process the request and return data as JSON
    data = {'message': 'Data from Django server'}
    return JsonResponse(data)


def new(request):
    return render(request, 'add_new_temp.html')


# to upload file by admin only

def file_list(request):
    files = ExcelDocument.objects.all()
    return render(request, 'file_list.html', {'files': files})


# for excel file upload
def view_excel(request, excel_id):
    excel_document = ExcelDocument.objects.get(pk=excel_id)

    # Read Excel data using pandas
    excel_data = pd.read_excel(excel_document.excel_file.path)

    # Convert the DataFrame to HTML
    excel_html = excel_data.to_html(
        classes='table table-bordered', index=False)

    return render(request, 'view_excel.html', {'excel_document': excel_document, 'excel_html': excel_html})


# yourapp/views.py
# def signup(request):
#     if request.method == "POST":
#         user_type = request.POST.get('user_type')
#         username = request.POST.get('usernumber')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')

#         if len(username) > 10 or len(username) < 10:
#             messages.info(request, "Phone Number Must be 10 Digits")
#             return redirect('/signup')

#         if pass1 != pass2:
#             messages.info(request, "Password is not Matching")
#             return redirect('/signup')

#         try:
#             if User.objects.get(username=username):
#                 messages.warning(request, "Phone Number is Taken")
#                 return redirect('/signup')

#         except Exception as identifier:
#             pass

#         try:
#             if User.objects.get(email=email):
#                 messages.warning(request, "Email is Taken")
#                 return redirect('/signup')

#         except Exception as identifier:
#             pass

#         myuser = CustomUser.objects.create_user(username, email, pass1)
#         myuser.save()
#         messages.success(request, "User is Created Please Login")
#         return redirect('/login')

#     return render(request, "signup.html")
