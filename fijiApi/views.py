from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class ConfederancyViewSet(viewsets.ModelViewSet):
    serializer_class = ConfederacySerializer
    queryset = Confederacy.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


class ProvincesViewSet(viewsets.ModelViewSet):
    serializer_class = ProvincesSerializer
    queryset = Provinces.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DistrictsViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictsSerializer
    queryset = Districts.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class VillageViewSet(viewsets.ModelViewSet):
    serializer_class = VillagesSerializer
    queryset = Villages.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


