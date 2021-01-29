from rest_framework import serializers
from .models import Department
 
class DepartmentSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Department
        fields = '__all__'