from django.urls import path
from .views import Dashboard
from . import views

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('fiji_confederacy/', views.getdashboard, name="fiji_confederacy"),
    path('district/', views.districts, name="district"),
    path('village/', views.village,name="village")

]