from django.contrib import admin

# Register your models here.
from .models import Instance_feature, Instance

admin.site.register(Instance_feature)
admin.site.register(Instance)
