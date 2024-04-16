from django.contrib import admin
from . models import *
# Register your models here.




@admin.register(ExcelDocument)
class ExcelAdmin(admin.ModelAdmin):
    list_display = ['id', 'field', 'uploaded_files']
    
    
# admin.site.register(WordDocument)
@admin.register(WordDocument)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'uploaded_files']
