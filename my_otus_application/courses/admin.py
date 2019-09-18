from django.contrib import admin
from django.contrib.auth.models import User
from . import models

admin.register(User)


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'id', 'course_name', 'description'


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'second_name', 'occupation'


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = 'id', 'start_date', 'description', 'teacher'
