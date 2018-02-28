from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import Solver, Instance
import pytest

def test_101():
    assert 10 % 2 == 0

@pytest.mark.django_db
def test_solver_post():
    factory = APIRequestFactory()
    data = {'name': 'choco', 'version':'2.0', 'source_path':'path1', 'executable_path': 'path2'}
    request = factory.post('/solvers/', data)
    queryset = Solver.objects.all()
    assert len(queryset) > 0
    solver = queryset[0]
    assert solver.name == 'choco'
