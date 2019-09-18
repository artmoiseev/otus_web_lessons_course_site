from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


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


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ("id", "username", "password",)
