from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import *



# Create your views here.
def writdata(request):
    with open('/home/sabiut/Documents/Fiji_data/confe.csv', 'r') as csvfile:
        readata = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in readata:
            if row[0]!= 'confederancy':
                _, created = Provinces.objects.get_or_create(
                confederancy=row[0],
                confederany_code=row[1],
                province_name =row[2],
                )


