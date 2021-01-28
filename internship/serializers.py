from rest_framework import serializers
from .models import Internship
 
class InternSerializers(serializers.ModelSerializer):

    class Meta:
        model= Internship
        fields = '__all__'