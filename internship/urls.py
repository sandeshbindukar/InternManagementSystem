from django.urls import path, include
from . import views
from .router import router

urlpatterns = [
    path('', views.index, name="home"),
    path('view_details/<str:intern_id>/', views.viewDetails, name="view_details"),
    path('api/interns/', include(router.urls)),
]