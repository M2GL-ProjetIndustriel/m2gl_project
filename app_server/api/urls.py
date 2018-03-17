from django.urls import path
from rest_framework.authtoken import views as tokenviews
from . import views
from .utils import *

urlpatterns = [
    path('', views.index, name='index'),
    path('instance', views.InstanceList.as_view()),
    path('instance/<int:pk>', views.InstanceDetail.as_view()),
    path('instanceFeature', views.InstanceFeatureList.as_view()),
    path('instanceFeature/<int:pk>', views.InstanceFeatureDetail.as_view()),
    path('solver', views.SolverList.as_view(), name='solver-list'),
    path('solver/<int:pk>', views.SolverDetail.as_view()),
    path('solver/<path:file_path>', views.DownloadFiles.as_view()),
    path('experiment', views.ExperimentationList.as_view()),
    path('experiment/<int:pk>', views.ExperimentationDetail.as_view()),
    path('result', views.ResultList.as_view()),
    path('result/<int:pk>', views.ResultDetail.as_view()),
    path('resultMeasurement', views.ResultMeasurementList.as_view()),
    path('resultMeasurement/<int:pk>', views.ResultMeasurementDetail.as_view()),
    path('token-auth', tokenviews.obtain_auth_token),
    path('user', views.UserList.as_view()),
    path('token', views.TokenList.as_view())
]

#create_dummy_user() # temp
init_tokens()
