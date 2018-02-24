from django.db import models

# Create your models here.

class Instance_feature(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    unit = models.CharField(max_length=100, blank=True)

class Instance(models.Model):
    name = models.CharField(max_length=100) # name of the problem ex: "100-queens"
    ptype = models.CharField(max_length=100) # type of problem. ex: "CSP" , "SAT" ...
    path = models.CharField(max_length=200, blank=True) # path to Instance file
    features = models.ManyToManyField(Instance_feature, blank=True)

class Solver(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100, blank=True)
    source_path = models.CharField(max_length=200, blank=True) # temporary until we find a better way of handling files.
    executable_path = models.CharField(max_length=200, blank=True) # temporary until we find a better way of handling files.

class Experimentation(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    solver_parameters = models.CharField(max_length=200)
    solver = models.ForeignKey(Solver, blank=True)
    device_info = models.CharField(max_length=200, blank=True)

class Result(models.Model):
    status = models.CharField(max_length=100)
    result = models.ForeignKey(Experimentation, on_delete=models.CASCADE)

class Result_Measurement(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=20, decimal_places=10)
    unit = models.CharField(max_length=100, blank=True)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
