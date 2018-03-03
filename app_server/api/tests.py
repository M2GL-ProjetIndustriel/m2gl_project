import pytest
from rest_framework.test import APITestCase
from time import sleep
from api.models import Solver


class SolverPostTest(APITestCase):
    data = {
        'name': 'choco',
        'version': '2.0',
        #TODO now server use FileField, good luck!!! :D
        #'source_path': 'path1',
        #'executable_path': 'path2'
    }

    def post(self):
        return self.client.post('/api/solver/', self.data)

    def test_post_status_should_be_201(self):
        response = self.post()
        assert response.status_code == 201

    @pytest.mark.django_db()
    def test_post_should_be_in_db(self):
        self.post()
        queryset = Solver.objects.all()
        solver = queryset[0]

        assert len(queryset) > 0

        assert solver.name == self.data['name']
        assert solver.version == self.data['version']
        #TODO now server use FileField, good luck!!! :D
        #assert solver.source_path == self.data['source_path']
        #assert solver.executable_path == self.data['executable_path']

    @pytest.mark.django_db()
    def test_should_have_created(self):
        self.post()
        queryset = Solver.objects.all()
        solver = queryset[0]

        assert solver.created

    @pytest.mark.django_db()
    def test_should_have_modified(self):
        self.post()
        queryset = Solver.objects.all()
        solver = queryset[0]
        assert solver.modified

    @pytest.mark.django_db()
    def test_initially_modified_should_be_equal_to_created(self):
        self.post()
        queryset = Solver.objects.all()
        solver = queryset[0]
        assert solver.modified.date() == solver.created.date()

    @pytest.mark.django_db()
    def test_put_after_post_should_be_different(self):
        self.post()
        queryset = Solver.objects.all()
        solver = queryset[0]
        assert solver.name == 'choco'

        sleep(2)
        response = self.client.put('/api/solver/' + str(solver.id), {
            'name': 'chocobon'
        })

        queryset = Solver.objects.all()
        solver = queryset[0]

        assert solver.name == 'chocobon'
        assert response.status_code == 200
        assert solver.modified.time() != solver.created.time()
