from django.test import TestCase, Client
from rest_framework import status

from .models import Teacher


# Create your tests here.

class TeacherTestCase(TestCase):
    def setUp(self) -> None:
        Teacher.objects.create(first_name="TestTeacherName", second_name="TestTeacherSecName", occupation="teacher")

    def test_str_teacher(self):
        teacher = Teacher.objects.get(first_name='TestTeacherName')
        assert str(teacher) == "TestTeacherName TestTeacherSecName"


class ViewsTest(TestCase):
    api_end_points = ['/', '/api/user', '/api/courses', '/api/teachers/', '/api/lessons/']

    def setUp(self) -> None:
        self.client = Client()

    def test_response_ok(self):
        for endpoint in self.api_end_points:
            with self.subTest():
                response = self.client.get(endpoint, follow=True)
                assert response.status_code == status.HTTP_200_OK

    def test_auth_with_valid_credentials(self):
        credentials = {
            "username": "user1",
            "password": "12345"
        }
        response = self.client.post('/api/auth/', data=credentials, follow=True)
        assert response.status_code == status.HTTP_200_OK

    def test_auth_with_bad_credentials(self):
        credentials = {
            "username": "user1",
            "password": "invalid_password"
        }
        response = self.client.post('/api/auth', data=credentials, follow=True)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

