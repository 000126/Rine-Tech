
from django.db import models

from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

ext_validator = FileExtensionValidator(['xlsx', 'xlsm', 'xltx'])

# for custom user creation


class Template(models.Model):
    template = models.FileField(
        upload_to='template', validators=[ext_validator])
    template_type = models.CharField(max_length=100)
    project_code = models.CharField(max_length=100)
    batch_no = models.IntegerField()
    a_r_no = models.IntegerField()

    def __str__(self):
        return self.project_code

# to view files


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template_name = models.CharField(max_length=100)
    template_type = models.CharField(max_length=255)
    template_number = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.template_name


# for excel file
# models.py


class ExcelDocument(models.Model):
    title = models.CharField(max_length=255)
    excel_file = models.FileField(upload_to='excels/')


# for custom user
# yourapp/models.py
