from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instances/', views.InstanceList.as_view()),
    path('instances/<int:pk>', views.InstanceDetail.as_view()),
    path('solver/', views.SolverList.as_view()),
    path('solver/<int:pk>', views.SolverDetail.as_view()),
    path('experiment/', views.ExperimentationList.as_view()),
    path('experiment/<int:pk>', views.ExperimentationDetail.as_view())
]
