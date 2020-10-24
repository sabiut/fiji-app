from django.urls import path
from .views import Dashboard
from . import views

urlpatterns = [
    path('dashboard/', Dashboard.as_view()),
    path('getdashboard/', views.getdashboard, name="getdashboard"),
    path('district/', views.districts, name="district"),
    path('village/', views.village,name="village")

]