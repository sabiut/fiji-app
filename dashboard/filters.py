from fijiApi.models import *
import django_filters
from django_filters import CharFilter

class villagefilter(django_filters.FilterSet):
    village_name = CharFilter(field_name='village_name',lookup_expr='icontains')
    class Meta:
        model = Villages
        fields ='__all__'
        exclude=['acknowledgement','district_code','district']