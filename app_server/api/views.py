from django.http import HttpResponse, Http404
from rest_framework import permissions, generics
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
import os


from .constants import *
from .models import Instance, Solver, Experimentation
from .serializers import (
    InstanceSerializer, SolverSerializer, ExperimentationSerializer
)


def index(_):
    return HttpResponse("Hello, world. You're at the api index.")


class StandardSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


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
    pagination_class = StandardSetPagination


@permission_classes((permissions.AllowAny,))
class ExperimentationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experimentation.objects.all()
    serializer_class = ExperimentationSerializer


@permission_classes((permissions.AllowAny,))
class SourcesFiles(APIView):
    def get(self, request, filename, format=None):
        file_name = request.path.split("/")[-1]
        file_path = DOWNLOADS_PATH + file_name
        try:
            fp = open(file_path, 'rb')
            response = HttpResponse(fp.read())
            fp.close()
            response['Content-Length'] = os.path.getsize(file_path)
        except FileNotFoundError:
            raise Http404("File does not exist")
        else:
            filename_header = 'filename=%s' % file_name
            response['Content-Disposition'] = 'attachment; ' + filename_header
        return response
