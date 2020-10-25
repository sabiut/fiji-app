from django.urls import path
from .views import Dashboard
from . import views

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('fiji_confederacy/', views.confederacy, name="fiji_confederacy"),
    path('province/', views.province, name = "province"),
    path('district/', views.districts, name="district"),
    path('village/', views.village,name="village")

]