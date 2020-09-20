from django.urls import path, include
from . import views
from rest_framework import  routers
from .views import *

router = routers.DefaultRouter()
router.register('confederacy', ConfederancyViewSet)
router.register('provinces', ProvincesViewSet)
router.register('districts', DistrictsViewSet)
router.register('villages', VillageViewSet)
router.register('contact', ContactViewSet)

urlpatterns = [
    #path('writdata', views.writdata, name="write_to")
    path('', include(router.urls))


]
