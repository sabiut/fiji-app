from django import  forms
from fijiApi.models import *

class update_villageForm(forms.ModelForm):
    class Meta:
        model = Villages
        fields = '__all__'


class add_confederacyForm(forms.ModelForm):
    class Meta:
        model = Confederacy
        fields ='__all__'

class add_provinceForm(forms.ModelForm):
    class Meta:
        model = Provinces
        fields ='__all__'


class add_districtForm(forms.ModelForm):
    class Meta:
        model = Districts
        fields ='__all__'

