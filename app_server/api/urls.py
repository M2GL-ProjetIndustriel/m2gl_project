from django.urls import path
from api.views import InstanceList, InstanceDetail
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instances/', views.InstanceList.as_view()),
    path(r'^instances/(?P<pk>[0-9]+)$', views.InstanceDetail.as_view())
]
