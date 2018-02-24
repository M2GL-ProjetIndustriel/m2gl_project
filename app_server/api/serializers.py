from rest_framework import serializers
from api.models import Instance_feature, Instance, Solver

class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = ('id', 'name', 'ptype', 'path')

    def create(self, validated_data):
        return Instance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.ptype = validated_data.get('ptype', instance.code)
        instance.path = validated_data.get('path', instance.path)
        instance.save()
        return instance

class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver
        fields = ('id', 'name', 'version', 'source_path', 'executable_path')

    def create(self, validated_data):
        return solver.objects.create(**validated_data)

    def update(self, solver, validated_data):
        solver.name = validated_data.get('name', solver.name)
        solver.ptype = validated_data.get('ptype', solver.code)
        solver.path = validated_data.get('path', solver.path)
        solver.save()
        return solver
