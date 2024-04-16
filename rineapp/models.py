from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


ext_validator = FileExtensionValidator(['xlsx', 'xlsm', 'xltx'])
val=FileExtensionValidator(['doc','docx'])



# for excel file


class ExcelDocument(models.Model):
    field = models.CharField(max_length=255)
    uploaded_files = models.FileField(
        upload_to='Uploaded files', validators=[ext_validator])



class WordDocument(models.Model):
    title = models.CharField(max_length=255)
    uploaded_files = models.FileField(upload_to='word_files/',validators=[val])