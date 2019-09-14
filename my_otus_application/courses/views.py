from django.http import HttpResponse
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


def index_view(request):
    return HttpResponse('<h1>Hello!</h1>')


class CourseListView(APIView):
    courses = models.Course.objects.all()
    serializer = serializers.CourseSerializer(courses, many=True)

    def get(self, request):
        return Response(self.serializer.data)


class TeacherListView(APIView):
    teachers = models.Teacher.objects.all()
    serializer = serializers.TeacherSerializer(teachers, many=True)

    def get(self, request):
        return Response(self.serializer.data)

    def post(self, request):
        return Response({"foo": "bar"})
