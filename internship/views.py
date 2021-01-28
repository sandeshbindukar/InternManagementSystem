from django.shortcuts import get_object_or_404, render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InternSerializers
from .models import Internship


def index(request):
    interns = Internship.objects.all()
    return render(request, 'index.html',
     {'interns':interns}
    )


def viewDetails(request, intern_id ):
    intern = get_object_or_404(Internship, id=intern_id)
    context = {"intern":intern}
    return render(request, 'view_details.html',context)


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Intern List':'/interns/',
        'Intern Detail View':'/interns/<str:pk>/',
        'Derpartment List':'/departments/',
        'Department Detail View':'/departments/<str:pk>/',
    }
    return Response(api_urls)


class InternList(APIView):

    def get(self,request):
        interns = Internship.objects.all()
        serializers = InternSerializers(interns, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = InternSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

 
class InternDetailView(APIView):
    
    def get(self,request, pk):
        interns = Internship.objects.get(id=pk)
        serializers = InternSerializers(interns, many=False)
        return Response(serializers.data)


@api_view(['POST'])
def createIntern(request):
    serializer = InternSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# class CreateIntern(APIView):

#     def post(request):
#         serializer = InternSerializers(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

