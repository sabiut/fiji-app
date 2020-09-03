from django.urls import path
from . import views

urlpatterns = [
    path('writdata', views.writdata, name="write_to")
]
