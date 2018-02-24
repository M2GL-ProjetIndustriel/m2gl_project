from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from api.serializers import InstanceSerializer
from api.models import Instance
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

# API views

@permission_classes((permissions.AllowAny,))
class InstanceList(APIView):
    """
    List all instances, or create a new instance.
    """

    def get(self, request, format=None):
        instances = Instance.objects.all()
        serializer = InstanceSerializer(instances, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstanceDetail(APIView):
    """
    Retrieve, update or delete an instance (problem instance) .
    """

    def get(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        serializer = InstanceSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        serializer = InstanceSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(Instance, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
