from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf

from .filters import villagefilter, confederacyfilter, districtfilter, dashboardfilter

# Create your views here.
from django.views import View
from fijiApi.models import *
from .forms import *


class Dashboard(View):
    def get(self, request):
        village = Villages.objects.all()
        myFilter = dashboardfilter(request.GET, queryset=village)
        village = myFilter.qs
        return render(request, 'dashboard.html', locals())


def confederacy(request):
    confederacy = Confederacy.objects.all()
    confederacyFilter = confederacyfilter(request.GET, queryset=confederacy)
    confederacy = confederacyFilter.qs
    return render(request, 'confederacy.html', locals())


def province(request):
    provinces = Provinces.objects.all()
    return render(request, 'provinces.html', locals())


def districts(request):
    districts = Districts.objects.all()
    districtFilter = districtfilter(request.GET, queryset=districts)
    districts = districtFilter.qs
    return render(request, 'districts.html', locals())


def village(request):
    village = Villages.objects.all()
    villageFilter = villagefilter(request.GET, queryset=village)
    village = villageFilter.qs
    return render(request, 'villages.html', locals())


@login_required(login_url='index')
def update_village_form(request, village_id):
    if request.method == 'POST':
        get_village_id = Villages.objects.get(id=village_id)
        village_form = update_villageForm(request.POST, instance=get_village_id)
        if village_form.is_valid():
            village_form.save()
            return render(request, 'village_thanks.html')

    else:
        get_village_id = Villages.objects.get(id=village_id)
        village_form = update_villageForm(instance=get_village_id)

    return render(request, 'update_village_form.html', locals())


@login_required(login_url='index')
def add_village(request):
    if request.POST:
        form = update_villageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/village')
    else:

        form = update_villageForm()
    return render(request, 'standard_add.html', {'form': form})


@login_required(login_url='index')
def add_confederacy(request):
    if request.POST:
        form = add_confederacyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'village_thanks.html')
    else:

        form = add_confederacyForm()
    return render(request, 'add_village_form.html', {'form': form})


@login_required(login_url='index')
def add_province(request):
    if request.POST:
        form = add_provinceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'village_thanks.html')
    else:

        form = add_provinceForm()
    return render(request, 'standard_add.html', {'form': form})


@login_required(login_url='index')
def add_district(request):
    if request.POST:
        form = add_districtForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'village_thanks.html')
    else:

        form = add_districtForm()
    return render(request, 'standard_add.html', {'form': form})


@login_required(login_url='index')
def update_condeferacy_form(request, village_id):
    if request.method == 'POST':
        get_confederacy_id = Confederacy.objects.get(id=village_id)
        form = add_confederacyForm(request.POST, instance=get_confederacy_id)
        if form.is_valid():
            form.save()
            return render(request, 'village_thanks.html')

    else:
        get_confederacy_id = Confederacy.objects.get(id=village_id)
        form = add_confederacyForm(instance=get_confederacy_id)

    return render(request, 'update_record_form.html', locals())


@login_required(login_url='index')
def update_province_form(request, village_id):
    if request.method == 'POST':
        get_province_id = Provinces.objects.get(id=village_id)
        form = add_provinceForm(request.POST, instance=get_province_id)
        if form.is_valid():
            form.save()
            return render(request, 'village_thanks.html')

    else:
        get_province_id = Provinces.objects.get(id=village_id)
        form = add_provinceForm(instance=get_province_id)

    return render(request, 'update_record_form.html', locals())


@login_required(login_url='index')
def update_district_form(request, village_id):
    if request.method == 'POST':
        get_district_id = Districts.objects.get(id=village_id)
        form = add_districtForm(request.POST, instance=get_district_id)
        if form.is_valid():
            form.save()
            return render(request, 'village_thanks.html')

    else:
        get_district_id = Districts.objects.get(id=village_id)
        form = add_districtForm(instance=get_district_id)

    return render(request, 'update_record_form.html', locals())
