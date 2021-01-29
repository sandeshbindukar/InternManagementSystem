from .viewsets import InternViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('internship', InternViewsets)