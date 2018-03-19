from django.db import models
from django.utils import timezone
from django.dispatch import receiver
import os.path
from .middleware import get_request

DOWNLOADS_PATH = './downloads/'

class Instance(models.Model):
    name = models.CharField(max_length=100)
    instance_type = models.CharField(max_length=100)
    instance_family = models.CharField(max_length=100, blank=True)
    path = models.CharField(max_length=200, blank=True)


class InstanceFeature(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    unit = models.CharField(max_length=100, blank=True)


class InstanceValue(models.Model):
    value = models.CharField(max_length=400)
    instance = models.ForeignKey(Instance, related_name='values',
        on_delete=models.CASCADE)
    feature = models.ForeignKey(InstanceFeature, on_delete=models.CASCADE)


def define_path(instance, filename):
    """
    Return the path where the files are downloaded. Also add the time at the end
    of the filename to differenciate files.
    """
    path_exist = True
    while path_exist:
        now = timezone.now()
        path_format = DOWNLOADS_PATH + '%Y/%m/%d/' + filename + '_%H%M%S%f'
        path_name = now.strftime(path_format)
        path_exist = os.path.isfile(path_name)
    return path_name


class Solver(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)
    source_path = models.FileField(upload_to=define_path, blank=True)
    executable_path = models.FileField(upload_to=define_path, blank=True)
    description = models.CharField(max_length=400, blank=True)
    owner = models.ForeignKey('auth.User', null=True, editable=False, on_delete=models.CASCADE)

    # from stackoverflow
    def save(self, *args, **kwargs):
        """ On creation set owner """
        user = get_request().user
        if user and user.is_authenticated:
            if not self.id:
                self.owner = user

        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Solver, self).save(*args, **kwargs)


def delete_file(filefield):
    """
        Take a filefield and delete the corresponding file from filesystem.
    """
    if filefield and os.path.isfile(filefield.path):
            os.remove(filefield.path)


@receiver(models.signals.post_delete, sender=Solver)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Solver` object is deleted.
    """
    delete_file(instance.source_path)
    delete_file(instance.executable_path)


@receiver(models.signals.pre_save, sender=Solver)
def save_old_filepath(sender, instance, **kwargs):
    """
    Save filename before update for deletion.
    """
    instance.old_source_path = None
    instance.old_executable_path = None

    if instance.pk:
        try:
            old_solver = Solver.objects.get(pk=instance.pk)

            instance.old_source_path = old_solver.source_path
            instance.old_executable_path = old_solver.executable_path
        except Solver.DoesNotExist:
            # Error raise when loadding data from fixtures.
            pass


def delete_old_file(filefield, old_filefield):
    """
    Delete a file replaced by a new one.
    """
    if old_filefield and filefield and filefield.path != old_filefield.path:
        delete_file(old_filefield)


@receiver(models.signals.post_save, sender=Solver)
def auto_delete_file_on_update(sender, instance, **kwargs):
    """
    Deletes olds files replaced during an update.
    """
    delete_old_file(instance.source_path, instance.old_source_path)
    delete_old_file(instance.executable_path, instance.old_executable_path)


class Experimentation(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    solver_parameters = models.CharField(max_length=200, blank=True)
    solver = models.ForeignKey(Solver, on_delete=models.CASCADE)
    device = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=400, blank=True)
    owner = models.ForeignKey('auth.User', null=True, editable=False, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """ On creation set owner """
        user = get_request().user
        if user and user.is_authenticated:
            if not self.id:
                self.owner = user

        return super(Experimentation, self).save(*args, **kwargs)

class Result(models.Model):
    status = models.CharField(max_length=100)
    experimentation = models.ForeignKey(Experimentation, on_delete=models.CASCADE)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)

class ResultMeasurement(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    unit = models.CharField(max_length=100, blank=True)


class ResultValue(models.Model):
    value = models.CharField(max_length=400)
    result = models.ForeignKey(Result, related_name='values',
        on_delete=models.CASCADE)
    measurement = models.ForeignKey(ResultMeasurement, on_delete=models.CASCADE)
