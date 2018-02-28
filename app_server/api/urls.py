from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instances/', views.InstanceList.as_view()),
    path('instances/<int:pk>', views.InstanceDetail.as_view()),
    path('solvers/', views.SolverList.as_view()),
    path('solvers/<int:pk>', views.SolverDetail.as_view()),
    path('experimentations/', views.ExperimentationList.as_view()),
    path('experimentations/<int:pk>', views.ExperimentationDetail.as_view())
]
