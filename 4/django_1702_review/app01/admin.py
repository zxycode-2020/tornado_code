#coding:utf8
from django.contrib import admin

# Register your models here.
import models

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('基本信息', {'fields': ['name','age','gender','group','avatar']}),
        ('其它信息', {'fields' : ['department'], 'classes': ['collapse']}),
    ]

    list_display = ['name','age','gender','date_add','date_modi']

    list_filter = ['department']

    search_fields = ['name','age']


admin.site.register(models.Employee,EmployeeAdmin)
admin.site.register(models.Department)
admin.site.register(models.Group)