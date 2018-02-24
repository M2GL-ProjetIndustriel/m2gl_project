from rest_framework import serializers
from api.models import Instance_feature, Instance

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
