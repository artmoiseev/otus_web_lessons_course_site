from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from pytz import unicode
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


def index_view(request):
    if request.user.is_authenticated:
        return HttpResponse(loader.get_template("index.html").render())
    return HttpResponse(loader.get_template("login_form.html").render())


class CourseListView(APIView):

    def get(self, request):
        courses = models.Course.objects.all()
        serializer = serializers.CourseSerializer(courses, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):

    def get(self, request, pk):
        course = get_object_or_404(models.Course, pk=pk)
        serializer = serializers.CourseSerializer(course)
        return Response(serializer.data)

    def patch(self, request, pk):
        course = get_object_or_404(models.Course, pk=pk)
        serializer = serializers.CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = get_object_or_404(models.Course, pk=pk)
        serializer = serializers.CourseSerializer(course)
        data = serializer.data
        course.delete()
        return Response(data)


class TeacherListView(APIView):

    def get(self, request):
        teachers = models.Teacher.objects.all()
        serializer = serializers.TeacherSerializer(teachers, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonsListView(APIView):

    def get(self, request):
        lessons = models.Lesson.objects.all()
        serializer = serializers.LessonSerializer(lessons, many=True)

        return Response(serializer.data)


class RegisterUserView(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User(APIView):
    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
