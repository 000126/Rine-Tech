from django.db import models
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.validators import FileExtensionValidator
# Create your models here.

ext_validator = FileExtensionValidator(['xlsx', 'xlsm', 'xltx'])


class Template(models.Model):
    template = models.FileField(
        upload_to='template', validators=[ext_validator])
    template_type = models.CharField(max_length=100)
    project_code = models.CharField(max_length=100)
    batch_no = models.IntegerField(max_length=100)
    a_r_no = models.IntegerField(max_length=100)

    def __str__(self):
        return self.project_code
