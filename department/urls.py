from django.urls import path, include
from . import views
from .router import router


urlpatterns = [
    path('departments/',views.viewDepartments, name="department" ),
    path('api/departments/', include(router.urls)),
]