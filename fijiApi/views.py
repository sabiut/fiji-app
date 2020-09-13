from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from url_filter.integrations.drf import DjangoFilterBackend


class ConfederancyViewSet(viewsets.ModelViewSet):
    serializer_class = ConfederacySerializer
    queryset = Confederacy.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['confederancy_name']
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProvincesViewSet(viewsets.ModelViewSet):
    serializer_class = ProvincesSerializer
    queryset = Provinces.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['province_name']
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


class DistrictsViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictsSerializer
    queryset = Districts.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['district_name']
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class VillageViewSet(viewsets.ModelViewSet):
    serializer_class = VillagesSerializer
    queryset = Villages.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['village_name']
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


