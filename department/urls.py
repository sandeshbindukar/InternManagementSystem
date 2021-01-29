from django.urls import path, include
from . import views


urlpatterns = [
    path('departments/',views.viewDepartments, name="department" ),
    
]