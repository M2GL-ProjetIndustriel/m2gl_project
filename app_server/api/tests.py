import pytest
from rest_framework.test import APITestCase

from api.models import Solver


class SolverTest(APITestCase):
    @pytest.mark.django_db()
    def test_correct_solver_post_should_return_201(self):
        response = self.client.post('/api/solver/', {
            'name': 'choco',
            'version': '2.0',
            'source_path': 'path1',
            'executable_path': 'path2'
        })
        assert response.status_code == 201
        queryset = Solver.objects.all()
        assert len(queryset) > 0
        solver = queryset[0]
        assert solver.name == 'choco'
