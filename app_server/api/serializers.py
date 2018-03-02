from rest_framework import serializers

from .models import Instance, Solver, Experimentation


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = ('id', 'name', 'problem_type', 'path')


class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver
        fields = ('id', 'name', 'add_date', 'version', 'source_path', 'executable_path')


class ExperimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experimentation
        fields = ('id', 'name', 'date', 'solver_parameters', 'solver', 'device')
