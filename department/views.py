from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DepartmentSerializers
from rest_framework.decorators import api_view

from .models import Department
# Create your views here.

def viewDepartments(request):
    departments = Department.objects.all()
    context={"departments":departments}
    return render(request, 'department.html',context)
    

class DepartmentList(APIView):
    
    def get(self,request):
        departments = Department.objects.all()
        serializers = DepartmentSerializers(departments, many=True)
        return Response(serializers.data)
    
    def post(self, request, *args, **kwargs):
        serializer = DepartmentSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class DepartmentDetailView(APIView):
    
    def get(self,request, pk):
        departments = Department.objects.get(id=pk)
        serializers = DepartmentSerializers(departments, many=False)
        return Response(serializers.data)



@api_view(['POST'])
def createDepartment(request):
    serializer = DepartmentSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

