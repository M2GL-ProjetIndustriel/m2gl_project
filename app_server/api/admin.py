from django.contrib import admin

from .models import *

admin.site.register(Instance)
admin.site.register(InstanceFeature)
admin.site.register(InstanceValue)
admin.site.register(Solver)
admin.site.register(Experimentation)
admin.site.register(Result)
admin.site.register(ResultMeasurement)
admin.site.register(ResultValue)
