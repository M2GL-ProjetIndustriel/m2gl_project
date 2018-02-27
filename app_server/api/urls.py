from django.urls import path, re_path
#from api.views import InstanceList, InstanceDetail, SolverList, SolverDetail, ExperimentationList, ExperimentationDetail
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instances/', views.InstanceList.as_view()),
    re_path(r'^instances/(?P<pk>[0-9]+)/$', views.InstanceDetail.as_view()),
    path('solvers/', views.SolverList.as_view()),
    re_path(r'^solvers/(?P<pk>[0-9]+)/$', views.SolverDetail.as_view()),
    path('experimentations/', views.ExperimentationList.as_view()),
    re_path(r'^experimentations/(?P<pk>[0-9]+)/$', views.ExperimentationDetail.as_view())
]
