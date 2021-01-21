from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('view_details/', views.view_details),
]