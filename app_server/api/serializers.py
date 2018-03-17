from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *


class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver
        fields = (
            'id',
            'name',
            'version',
            'created',
            'modified',
            'source_path',
            'executable_path',
            'description',
            'owner'
        )


class ExperimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experimentation
        fields = (
            'id',
            'name',
            'date',
            'solver_parameters',
            'solver',
            'device',
            'description',
            'owner'
            )


class ResultValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultValue
        fields = ('id', 'value', 'measurement')


class ResultSerializer(WritableNestedModelSerializer):
    values = ResultValueSerializer(many=True)

    class Meta:
        model = Result
        fields = ('id', 'status', 'experimentation', 'instance', 'values')


class ResultMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultMeasurement
        fields = ('id', 'name', 'unit')


class InstanceValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstanceValue
        fields = ('id', 'value', 'feature')


class InstanceSerializer(WritableNestedModelSerializer):
    values = InstanceValueSerializer(many=True)

    class Meta:
        model = Instance
        fields = ('id', 'name', 'instance_type', 'instance_family', 'path', 'values')


class InstanceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstanceFeature
        fields = ('id', 'name', 'unit')
