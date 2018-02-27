from rest_framework import serializers
from api.models import Instance_feature, Instance, Solver, Experimentation

class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = ('id', 'name', 'ptype', 'path')

class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver
        fields = ('id', 'name', 'version', 'source_path', 'executable_path')

class ExperimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experimentation
        fields = ('id', 'name', 'date', 'solver_parameters', 'solver',
            'device_info')
