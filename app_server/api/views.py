from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
import os.path
import pathlib
from urllib.parse import quote

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
class DownloadFiles(APIView):
    def get(self, request, pk, format=None):
        solver = get_object_or_404(Solver.objects.all(), pk=pk)
        #Choose between executable and source file
        if request.path.split('/')[-1] == 'source':
            file_path = solver.source_path.name
            type_file = 'source'
        else:
            file_path = solver.executable_path.name
            type_file = 'executable'
        extension = ''.join(pathlib.Path(file_path).suffixes)
        send_file_name = solver.name + '_' + type_file + extension
        response = self.response_from_file(file_path, send_file_name)
        return response

    def response_from_file(self, file_path, send_file_name):
        try:
            fp = open(file_path, 'rb')
            response = HttpResponse(fp.read())
            fp.close()

            response['Content-Length'] = os.path.getsize(file_path)
            filename_header = 'filename*=UTF-8\'\'%s' % quote(
                send_file_name.encode('utf-8'))
            response['Content-Disposition'] = 'attachment; ' + filename_header
        except FileNotFoundError:
            raise Http404("File does not exist")
        return response
