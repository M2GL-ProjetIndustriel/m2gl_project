from django.db import models

# Create your models here.
class Instance(models.Model):
    name = models.CharField(max_length=100) # name of the problem ex: "100-queens"
    ptype = models.CharField(max_length=100) # type of problem. ex: "CSP" , "SAT" ...
    path = models.CharField(max_length=200, blank=True) # path to Instance file

class Instance_feature(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100, blank=True)

class Instance_value(models.Model):
    value = models.CharField(max_length=400)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    feature = models.ForeignKey(Instance_feature, on_delete=models.CASCADE)

class Solver(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100, blank=True)
    source_path = models.CharField(max_length=200, blank=True) # temporary until we find a better way of handling files.
    executable_path = models.CharField(max_length=200, blank=True) # temporary until we find a better way of handling files.

#TODO add User
class Experimentation(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    solver_parameters = models.CharField(max_length=200)
    solver = models.ForeignKey(Solver, on_delete=models.CASCADE)
    device_info = models.CharField(max_length=200, blank=True)

class Result(models.Model):
    status = models.CharField(max_length=100)
    result = models.ForeignKey(Experimentation, on_delete=models.CASCADE)

class Result_Measurement(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100, blank=True)

class Result_value(models.Model):
    value = models.CharField(max_length=400)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Result_Measurement, on_delete=models.CASCADE)
