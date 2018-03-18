from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import Permission
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
import os.path
import pathlib
from urllib.parse import quote
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
import pdb
from .models import *
from .serializers import *


class CustomPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'results': data
        })

#Same as default ordering but with sort and order parameters in place of ordering
class CustomOrderingFilter(filters.OrderingFilter):
    def get_ordering(self, request, queryset, view):
        default_ordering = "%s" % (getattr(view, 'ordering', ''),)
        sort = request.query_params.get('sort', default_ordering)
        order = request.query_params.get('order', '')

        #Add an ordering parameters to the query
        mutable = request.query_params._mutable
        request.query_params._mutable = True
        request.query_params['ordering'] = ('-' + sort if order == 'desc'
            else sort)
        request.query_params._mutable = mutable

        return super().get_ordering(request, queryset, view)


def index(_):
    return HttpResponse("Hello, world. You're at the api index.")

class UserInfo(APIView):
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAdminUser,)
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, )

    def get(self, request, *args, **kwargs):
        try:
            #token_key = self.request.query_params.get('token')
            token_key = kwargs['token']
            token = Token.objects.get(key=token_key)
            # retrieve user corresponding to token
            user = token.user
            username = user.username
            user_id = user.pk
            # get user's permissions
            p_list = Permission.objects.filter(user=user)
            permissions = [ x.name for x in p_list]
            data = { 'username': username, 'user_id': user_id, 'permissions': permissions }

        except Exception:
            raise Http404('Invalid token.')

        return(Response(data))

class SolverDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Solver.objects.all()
    serializer_class = SolverSerializer

# API views
class InstanceList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    pagination_class = CustomPagination
    filter_backends = (CustomOrderingFilter, filters.SearchFilter,
        DjangoFilterBackend)
    search_fields = ('id', 'name', 'instance_type', 'instance_family', 'path')
    filter_fields = ('id', 'name', 'instance_type', 'instance_family', 'path')
    ordering_fields = '__all__'
    ordering = ('id',)


class InstanceDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer


class InstanceFeatureList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = InstanceFeature.objects.all()
    serializer_class = InstanceFeatureSerializer
    pagination_class = CustomPagination
    filter_backends = (CustomOrderingFilter, filters.SearchFilter,
        DjangoFilterBackend)
    search_fields = ('name', 'unit', 'id')
    filter_fields = ('name', 'unit', 'id')
    ordering_fields = '__all__'
    ordering = ('id',)


class InstanceFeatureDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = InstanceFeature.objects.all()
    serializer_class = InstanceFeatureSerializer


class SolverList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Solver.objects.all()
    serializer_class = SolverSerializer
    pagination_class = CustomPagination
    filter_backends = (CustomOrderingFilter, filters.SearchFilter,
        DjangoFilterBackend)
    search_fields = ('id', 'name', 'version', 'created', 'modified',
        'source_path', 'executable_path')
    filter_fields = ('id', 'name', 'version', 'created', 'modified')
    ordering_fields = '__all__'
    ordering = ('id',)


class SolverDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Solver.objects.all()
    serializer_class = SolverSerializer


class ExperimentationList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Experimentation.objects.all()
    serializer_class = ExperimentationSerializer
    pagination_class = CustomPagination
    filter_backends = (CustomOrderingFilter, filters.SearchFilter,
        DjangoFilterBackend)
    search_fields = ('date', 'device', 'id', 'name', 'solver_parameters')
    filter_fields = ('date', 'device', 'id', 'name', 'solver_parameters')
    ordering_fields = '__all__'
    ordering = ('id',)


class ExperimentationDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Experimentation.objects.all()
    serializer_class = ExperimentationSerializer


class ResultList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    pagination_class = CustomPagination
    filter_backends = (CustomOrderingFilter, filters.SearchFilter,
        DjangoFilterBackend)
    search_fields = ('status', 'id')
    filter_fields = ('status', 'id')
    ordering_fields = '__all__'
    ordering = ('id',)


class ResultDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultMeasurementList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = ResultMeasurement.objects.all()
    serializer_class = ResultMeasurementSerializer
    pagination_class = CustomPagination
    filter_backends = (CustomOrderingFilter, filters.SearchFilter,
        DjangoFilterBackend)
    search_fields = ('name', 'unit', 'id')
    filter_fields = ('name', 'unit', 'id')
    ordering_fields = '__all__'
    ordering = ('id',)


class ResultMeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = ResultMeasurement.objects.all()
    serializer_class = ResultMeasurementSerializer


class DownloadFiles(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, file_path, format=None):
        # Extract filename from path and cut the time "differentiator" (added
        # when the file was upload).
        send_file_name = file_path.split('/')[-1].rsplit('_', 1)[0]
        response = self.make_response_from_file(file_path, send_file_name)
        return response

    # Create a response object base on a file
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
