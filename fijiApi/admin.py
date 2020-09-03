from django.contrib import admin
from django.contrib.admin import site


# Register your models here.
from . models import *
admin.site.register(Confederacy)
admin.site.register(Provinces)
admin.site.register(Districts)
admin.site.register(Villages)
