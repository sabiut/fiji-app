from fijiApi.models import *
import django_filters
from django_filters import CharFilter

class dashboardfilter(django_filters.FilterSet):
    village_name = CharFilter(field_name='village_name',lookup_expr='icontains')
    class Meta:
        model = Villages
        fields ='__all__'
        exclude=['acknowledgement','district_code','district']


class confederacyfilter(django_filters.FilterSet):
    confederacy_name = CharFilter(field_name='confederancy_name',lookup_expr='icontains')
    class Meta:
        model = Confederacy
        fields ='__all__'
        exclude = ['confederancy_name']

class districtfilter(django_filters.FilterSet):
    district_name = CharFilter(field_name='district_name',lookup_expr='icontains')
    class Meta:
        model = Districts
        fields ='__all__'
        exclude = ['confederancy','province','province_code']


class villagefilter(django_filters.FilterSet):
    village_name = CharFilter(field_name='village_name',lookup_expr='icontains')
    class Meta:
        model = Villages
        fields ='__all__'
        exclude = ['confederancy','province','district_code','district','acknowledgement']

