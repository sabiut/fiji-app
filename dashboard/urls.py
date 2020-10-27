from django.urls import path
from .views import Dashboard
from . import views

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('fiji_confederacy/', views.confederacy, name="fiji_confederacy"),
    path('province/', views.province, name="province"),
    path('district/', views.districts, name="district"),
    path('village/', views.village, name="village"),
    # update village form
    path('<int:village_id>/update_confederacy/', views.update_condeferacy_form, name="update_confederacy"),
    path('<int:village_id>/update_province/', views.update_province_form, name="update_province"),
    path('<int:village_id>/update_district/', views.update_district_form, name="update_district"),
    path('<int:village_id>/update_village/', views.update_village_form, name="update_village"),
    path('add_confederacy/', views.add_confederacy, name="add_confederacy"),
    path('add_province/', views.add_province, name="add_province"),
    path('add_district/', views.add_district, name="add_district"),
    path('add_village/', views.add_village, name="add_village")

]
