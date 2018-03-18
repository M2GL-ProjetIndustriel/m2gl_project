from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
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


class ResultMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultMeasurement
        fields = ('id', 'name', 'unit')


class ResultValueSerializer(serializers.ModelSerializer):
    measurement = ResultMeasurementSerializer(read_only=True)
    measurement_id = serializers.PrimaryKeyRelatedField(source='measurement',
        queryset=ResultMeasurement.objects.all())

    class Meta:
        model = ResultValue
        fields = ('id', 'value', 'measurement', 'measurement_id')


class ResultSerializer(WritableNestedModelSerializer):
    values = ResultValueSerializer(many=True)

    class Meta:
        model = Result
        fields = ('id', 'status', 'experimentation', 'instance', 'values')


class InstanceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstanceFeature
        fields = ('id', 'name', 'unit')


class InstanceValueSerializer(serializers.ModelSerializer):
    feature = InstanceFeatureSerializer(read_only=True)
    feature_id = serializers.PrimaryKeyRelatedField(source='feature',
        queryset=InstanceFeature.objects.all())

    class Meta:
        model = InstanceValue
        fields = ('id', 'value', 'feature', 'feature_id')


class InstanceSerializer(WritableNestedModelSerializer):
    values = InstanceValueSerializer(many=True)

    class Meta:
        model = Instance
        fields = ('id', 'name', 'instance_type', 'instance_family', 'path',
            'values')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('id', 'username')


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields= ('id', 'user', 'key')
