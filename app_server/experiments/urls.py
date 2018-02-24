from django.urls import path
from experiments.views import InstanceList, InstanceDetail
from experiments import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instances/', views.InstanceList.as_view()),
    path(r'^instances/(?P<pk>[0-9]+)$', views.InstanceDetail.as_view())
]
