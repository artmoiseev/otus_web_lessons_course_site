from django.test import TestCase, Client

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
                assert response.status_code == 200
