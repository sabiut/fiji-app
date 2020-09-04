from rest_framework import serializers
from .models import *

class ConfederacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Confederacy
        fields = ('confederancy_name',)

class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = (
            'confederancy',
            'confederancy_code',
            'province_name',
        )

class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = (
            'province',
            'province_code',
            'district_name',
        )

class VillagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villages
        fields = (
            'district',
            'district_code',
            'village_name',
            'acknowledgement',
        )
