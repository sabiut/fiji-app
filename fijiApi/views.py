from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import *
from rest_framework import viewsets
from .serializers import *


class ConfederancyViewSet(viewsets.ModelViewSet):
    serializer_class = ConfederacySerializer
    queryset = Confederacy.objects.all()


class ProvincesViewSet(viewsets.ModelViewSet):
    serializer_class = ProvincesSerializer
    queryset = Provinces.objects.all()


class DistrictsViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictsSerializer
    queryset = Districts.objects.all()


class VillageViewSet(viewsets.ModelViewSet):
    serializer_class = VillagesSerializer
    queryset = Villages.objects.all()


