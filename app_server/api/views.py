from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status, generics

from api.serializers import InstanceSerializer, SolverSerializer, ExperimentationSerializer
from api.models import Instance, Solver, Experimentation

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

# API views

@permission_classes((permissions.AllowAny,))
class InstanceList(generics.ListCreateAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

@permission_classes((permissions.AllowAny,))
class InstanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer


@permission_classes((permissions.AllowAny,))
class SolverList(generics.ListCreateAPIView):
    queryset = Solver.objects.all()
    serializer_class = SolverSerializer

@permission_classes((permissions.AllowAny,))
class SolverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solver.objects.all()
    serializer_class = SolverSerializer


@permission_classes((permissions.AllowAny,))
class ExperimentationList(generics.ListCreateAPIView):
    queryset = Experimentation.objects.all()
    serializer_class = ExperimentationSerializer

@permission_classes((permissions.AllowAny,))
class ExperimentationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experimentation.objects.all()
    serializer_class = ExperimentationSerializer
