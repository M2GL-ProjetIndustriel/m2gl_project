from django.contrib import admin

# Register your models here.
from .models import InstanceFeature, Instance, Solver

admin.site.register(InstanceFeature)
admin.site.register(Instance)
admin.site.register(Solver)
