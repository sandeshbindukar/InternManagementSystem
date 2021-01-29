from django.shortcuts import render
from .models import Department
from rest_framework import viewsets
from . import serializers

def viewDepartments(request):
    departments = Department.objects.all()
    context={"departments":departments}
    return render(request, 'department.html',context)


class DepartmentList(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializers