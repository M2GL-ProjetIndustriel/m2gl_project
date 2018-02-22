from django.db import models

# Create your models here.

class Instance(models.Model):
    name = models.CharField(max_length=100)
    ptype = models.CharField(max_length=30)
    path = models.CharField(max_length=200)

class Instance_feature(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=30)
