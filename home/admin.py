from operator import imod
from django.contrib import admin
from home.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(School)

class ViewAdmin(ImportExportModelAdmin):
    pass