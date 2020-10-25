
from django.shortcuts import render

# Create your views here.
from django.views import View
from fijiApi.models import *


class Dashboard(View):
    def get(self, request):
        village = Villages.objects.all()
        return render(request, 'dashboard.html',locals())

def confederacy(request):
    confederacy = Confederacy.objects.all()
    return render(request, 'confederacy.html', locals())

def province(request):
    provinces = Provinces.objects.all()
    return render(request, 'provinces.html', locals())

def districts(request):
    districts = Districts.objects.all()
    return render(request, 'districts.html', locals())


def village(request):
    village =Villages.objects.all()
    return render(request, 'villages.html', locals())