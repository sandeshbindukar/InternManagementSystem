from .viewsets import DepartmentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('department', DepartmentViewset)