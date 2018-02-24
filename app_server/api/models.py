from django.db import models

# Create your models here.

class Instance_feature(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)

class Instance(models.Model):
    name = models.CharField(max_length=100) # name of the problem ex: "100-queens"
    ptype = models.CharField(max_length=100) # type of problem. ex: "CSP" , "SAT" ...
    path = models.CharField(max_length=200, blank=True) # path to Instance file
    features = models.ManyToManyField(Instance_feature, blank=True)

class Solver(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100, blank=True)
    source_path = models.CharField(max_length=200, blank=True) # temporary until we find a better way of handleing files.
    executable_path = models.CharField(max_length=200, blank=True) # temporary until we find a better way of handleing files.
