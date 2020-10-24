
from django.shortcuts import render

# Create your views here.
from django.views import View
from fijiApi.models import *


class Dashboard(View):
    def get(self, request):
        data = Confederacy.objects.all()
        return render(request, 'dashboard.html',locals())

def getdashboard(request):
    province = Provinces.objects.all()
    return render(request, 'provinces.html', locals())

def districts(request):
    districts = Districts.objects.all()
    return render(request, 'districts.html', locals())


def village(request):
    village =Villages.objects.all()
    return render(request, 'villages.html', locals())