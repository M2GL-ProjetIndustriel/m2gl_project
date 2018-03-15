import pytest
from rest_framework.test import APITestCase
from time import sleep
from api.models import Solver
from django.urls import reverse
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class SolverPostTest(APITestCase):
    data = {
        'name': 'choco',
        'version': '2.0',
    }

    def setUp(self):
        self.data['source_path'] = SimpleUploadedFile("source.txt",
            b"file_content")
        self.data['executable_path'] = SimpleUploadedFile("exe.txt",
            b"file_content")

    def tearDown(self):
        queryset = Solver.objects.all()
        solver = queryset[0]

        if os.path.isfile(solver.source_path.path):
            os.remove(solver.source_path.path)

        if os.path.isfile(solver.executable_path.path):
            os.remove(solver.executable_path.path)

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
        assert os.path.isfile(solver.source_path.path)
        assert os.path.isfile(solver.executable_path.path)

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
        old_source_path = solver.source_path.path

        sleep(2)
        new_file = SimpleUploadedFile("source2.txt", b"file_content")
        response = self.client.put('/api/solver/' + str(solver.id), {
            'name': 'chocobon', 'source_path': new_file
        })

        queryset = Solver.objects.all()
        solver = queryset[0]

        assert solver.name == 'chocobon'
        assert response.status_code == 200
        assert solver.modified.time() != solver.created.time()
        assert solver.source_path.path != old_source_path
        assert os.path.isfile(solver.source_path.path)
        assert not os.path.isfile(old_source_path)


class SolverGetTest(APITestCase):

    def test_get_solver_list_ok(self):
        url = reverse('solver-list')
        response = self.client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db()
    def test_get_solver_detail_ok(self):
        solver = Solver.objects.create(name='choco', version='v2.0')
        url = '/api/solver/' + str(solver.id)
        response = self.client.get(url)
        assert response.status_code == 200
        data = response.data

        assert data['name'] == 'choco'
        assert data['version'] == 'v2.0'

    def test_get_solver_detail_ko(self):
        url = 'api/solver/10'
        response = self.client.get(url)
        assert response.status_code == 404

    def test_get_solver_file(self):
        pass

    def test_get_solver_file_ko(self):
        pass
