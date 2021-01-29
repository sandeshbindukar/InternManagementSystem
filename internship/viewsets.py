from rest_framework import viewsets
from . import models
from . import serializers

class InternViewsets(viewsets.ModelViewSet):
    queryset = models.Internship.objects.all()
    serializer_class = serializers.InternSerializers