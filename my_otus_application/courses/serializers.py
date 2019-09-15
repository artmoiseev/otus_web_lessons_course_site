from rest_framework import serializers
from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = 'id', 'course_name', 'description', 'price', 'teachers', 'lessons'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = 'id', 'first_name', 'second_name', 'occupation'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        exclude = tuple()
