from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
import os.path
import pathlib
from urllib.parse import quote

from .models import Instance, Solver, Experimentation
from .serializers import (
    InstanceSerializer, SolverSerializer, ExperimentationSerializer
)


def index(_):
    return HttpResponse("Hello, world. You're at the api index.")


class CustomPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'results': data
        })

# API views
@permission_classes((permissions.AllowAny,))
class InstanceList(generics.ListCreateAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    pagination_class = CustomPagination

@permission_classes((permissions.AllowAny,))
class InstanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer


@permission_classes((permissions.AllowAny,))
class SolverList(generics.ListCreateAPIView):
    queryset = Solver.objects.all()
    serializer_class = SolverSerializer
    pagination_class = CustomPagination


@permission_classes((permissions.AllowAny,))
class SolverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solver.objects.all()
    serializer_class = SolverSerializer


@permission_classes((permissions.AllowAny,))
class ExperimentationList(generics.ListCreateAPIView):
    queryset = Experimentation.objects.all()
    serializer_class = ExperimentationSerializer
    pagination_class = CustomPagination


@permission_classes((permissions.AllowAny,))
class ExperimentationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experimentation.objects.all()
    serializer_class = ExperimentationSerializer


@permission_classes((permissions.AllowAny,))
class DownloadFiles(APIView):
    def get(self, request, pk, format=None):
        solver = get_object_or_404(Solver.objects.all(), pk=pk)
        # Use to know witch file to send (source or executable)
        url_type = request.path.split('/')[-1]
        path_field = (solver.source_path if url_type == 'source'
            else solver.executable_path)
        file_path = path_field.name
        # Extract filename from path and cut the time "differentiator" (added
        # when the file was upload).
        send_file_name = file_path.split('/')[-1].rsplit('_', 1)[0]
        response = self.make_response_from_file(file_path, send_file_name)
        return response

    def make_response_from_file(self, file_path, send_file_name):
        try:
            fp = open(file_path, 'rb')
            response = HttpResponse(fp.read())
            fp.close()
            send_file_name_utf8 = quote(send_file_name.encode('utf-8'))
            filename_header = 'filename*=UTF-8\'\'%s' % send_file_name_utf8
            response['Content-Disposition'] = 'attachment; ' + filename_header
            response['Content-Length'] = os.path.getsize(file_path)
        except FileNotFoundError:
            raise Http404("File does not exist")
        return response
