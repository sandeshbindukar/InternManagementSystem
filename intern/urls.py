"""intern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from department.models import Department
import internship
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from internship.views import InternList, apiOverView, InternDetailView, createIntern
from department.views import DepartmentList, DepartmentDetailView, createDepartment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', apiOverView ),
    # path('api/interns/', InternList.as_view() ),
    # path('api/interns/<str:pk>/', InternDetailView.as_view() ),
    # path('api/departments/', DepartmentList.as_view()),
    # path('api/departments/<str:pk>/', DepartmentDetailView.as_view()),
    # path('create-intern/', createIntern),
    # path('create-department/', createDepartment),
    path('', include(('internship.urls','internship'), namespace='internship')),
    path('',include(('department.urls','department'), namespace='department')),
 
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)