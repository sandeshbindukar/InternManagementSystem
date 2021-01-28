from internship.models import Internship
from django.contrib import admin

# Register your models here.
class InternshipAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'email_address', 'date_of_birth' , 'phone_number', 'department', 'start_date', 'end_date', 'current_address', 'permanent_address', 'image']

admin.site.register(Internship, InternshipAdmin)   