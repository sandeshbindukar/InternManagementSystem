from rest_framework import serializers
from .models import Internship
 
class InternSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Internship
        fields = '__all__'