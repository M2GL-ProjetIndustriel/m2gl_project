from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = ('id', 'name', 'problem_type', 'path')


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
            'executable_path'
        )


class ExperimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experimentation
        fields = ('id', 'name', 'date', 'solver_parameters', 'solver', 'device')


class ResultValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultValue
        fields = ('id', 'value', 'result')


class ResultValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultValue
        fields = ('id', 'value', 'measurement')


class ResultSerializer(WritableNestedModelSerializer):
    values = ResultValueSerializer(many=True)

    class Meta:
        model = Result
        fields = ('id', 'status', 'experimentation', 'values')


class ResultMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultMeasurement
        fields = ('id', 'name', 'unit')
