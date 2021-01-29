from django.shortcuts import get_object_or_404, render
from .models import Internship
from rest_framework import viewsets
from . import models
from . import serializers


def index(request):
    interns = Internship.objects.all()
    return render(request, 'index.html',
     {'interns':interns}
    )


def viewDetails(request, intern_id ):
    intern = get_object_or_404(Internship, id=intern_id)
    context = {"intern":intern}
    return render(request, 'view_details.html',context)


class InternList(viewsets.ModelViewSet):
    queryset = models.Internship.objects.all()
    serializer_class = serializers.InternSerializers

