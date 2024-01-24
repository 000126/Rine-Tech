from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . models import *
import pandas as pd
from .models import ExcelDocument


def index(request):
    return render(request, 'index.html')


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


# @csrf_exempt
# def get_data(request):
#     # Process the request and return data as JSON
#     data = {'message': 'Data from Django server'}
#     return JsonResponse(data)


def new(request):
    return render(request, 'add_new_temp.html')


# to upload file by admin only

def file_list(request):
    files = ExcelDocument.objects.all()
    return render(request, 'file_list.html', {'files': files})


# for excel file upload
def view_excel(request, excel_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login and Try Again")
        return redirect('/auth/login/')
    excel_document = ExcelDocument.objects.get(pk=excel_id)

    # Read Excel data using pandas
    excel_data = pd.read_excel(excel_document.excel_file.path)

    # Convert the DataFrame to HTML
    excel_html = excel_data.to_html(
        classes='table table-bordered', index=False)

    return render(request, 'view_excel.html', {'excel_document': excel_document, 'excel_html': excel_html})
