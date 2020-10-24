from rest_framework import serializers
from .models import *

class ConfederacySerializer(serializers.ModelSerializer):
    province = serializers.StringRelatedField(many=True)
    district = serializers.StringRelatedField(many=True)
    village = serializers.StringRelatedField(many=True)


    class Meta:
        model = Confederacy
        fields = ('id','confederancy_name',
                  'province','district','village')




class ProvincesSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(many=True)

    class Meta:
        model = Provinces
        fields = (
            'id',
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
            'id',
            'confederancy',
            'province',
            'province_code',
            'district_name',
            'village',

        )


class VillagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villages
        fields = (
            'id',
            'confederancy',
            'district',
            'district_code',
            'village_name',
            'acknowledgement',
        )

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model =contact
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'message'
        )

