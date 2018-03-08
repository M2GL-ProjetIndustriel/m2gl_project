from django.urls import path
from rest_framework.authtoken import views as tokenviews
from . import views
from .utils import *

urlpatterns = [
    path('', views.index, name='index'),
    path('instances/', views.InstanceList.as_view()),
    path('instances/<int:pk>', views.InstanceDetail.as_view()),
    path('solver/', views.SolverList.as_view(), name='solver-list'),
    path('solver/<int:pk>', views.SolverDetail.as_view()),
    path('solver/<path:file_path>', views.DownloadFiles.as_view()),
    path('experimentation/', views.ExperimentationList.as_view()),
    path('experimentation/<int:pk>', views.ExperimentationDetail.as_view()),
    path('token-auth/', tokenviews.obtain_auth_token)
]

create_dummy_user() # temp
init_tokens()
