from rest_framework import serializers
from .models import *


class ConfederacySerializer(serializers.ModelSerializer):
    province = serializers.StringRelatedField(many=True)

    class Meta:
        model = Confederacy
        fields = ('confederancy_name',
                  'province',)


class ProvincesSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(many=True)

    class Meta:
        model = Provinces
        fields = (
            'confederancy',
            'confederancy_code',
            'province_name',
            'district',
        )


class DistrictsSerializer(serializers.ModelSerializer):
    village = serializers.StringRelatedField(many=True)

    class Meta:
        model = Districts
        fields = (
            'province',
            'province_code',
            'district_name',
            'village',

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
