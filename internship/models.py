from department.models import Department
from django.db import models


class Internship(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15)
    current_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

