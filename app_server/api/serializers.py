from rest_framework import serializers
from api.models import Instance_feature, Instance, Solver, Experimentation

class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = ('id', 'name', 'ptype', 'path')

    def create(self, validated_data):
        return Instance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.ptype = validated_data.get('ptype', instance.ptype)
        instance.path = validated_data.get('path', instance.path)
        instance.save()
        return instance

class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver
        fields = ('id', 'name', 'version', 'source_path', 'executable_path')

    def create(self, validated_data):
        return Solver.objects.create(**validated_data)

    def update(self, solver, validated_data):
        solver.name = validated_data.get('name', solver.name)
        solver.ptype = validated_data.get('ptype', solver.ptype)
        solver.path = validated_data.get('path', solver.path)
        solver.save()
        return solver


class ExperimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experimentation
        fields = ('id', 'name', 'date', 'solver_parameters', 'solver',
            'device_info')

    # vvv Inutile?
    """
    def create(self, validated_data):
        return experimentation.objects.create(**validated_data)

    def update(self, solver, validated_data):
        experimentation.name = validated_data.get('name', experimentation.name)
        experimentation.date = validated_data.get('date', experimentation.date)
        experimentation.solver_parameters = validated_data.get('solver_parameters',
            experimentation.solver_parameters)
        experimentation.solver = validated_data.get('solver', experimentation.solver)
        experimentation.device_info = validated_data.get('device_info',
            experimentation.device_info)
        experimentation.save()
        return experimentation
    """
