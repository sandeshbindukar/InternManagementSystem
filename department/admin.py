from department.models import Department
from django.contrib import admin


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Department, DepartmentAdmin)   