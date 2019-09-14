from django.contrib import admin

from . import models


# Register your models here.

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'description'


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'second_name', 'occupation'


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = 'id', 'start_date', 'description', 'teacher'
