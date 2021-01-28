from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('view_details/<str:intern_id>/', views.viewDetails, name="view_details"),
]