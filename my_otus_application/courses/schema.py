import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from . import models


class CourseType(DjangoObjectType):
    class Meta:
        model = models.Course
        filter_fields = {
            'id': ['exact'],
            'course_name': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
        }

        interfaces = (graphene.Node,)


class TeacherType(DjangoObjectType):
    class Meta:
        model = models.Teacher


class Query:
    all_courses = graphene.List(CourseType)
    all_teachers = graphene.List(TeacherType)

    filtered_courses = DjangoFilterConnectionField(CourseType)

    course = graphene.Field(CourseType, id=graphene.Int(), course_name=graphene.String())
    teacher = graphene.Field(TeacherType, id=graphene.Int())

    def resolve_all_courses(self, info, **kwargs):
        return models.Course.objects.all()

    def resolve_all_teachers(self, info, **kwargs):
        return models.Teacher.objects.all()

    def resolve_course(self, info, **kwargs):
        if 'id' in kwargs:
            return models.Course.objects.get(id=kwargs['id'])
        if 'course_name' in kwargs:
            return models.Course.objects.get(course_name=kwargs['course_name'])

    def resolve_teacher(self, info, **kwargs):
        if 'id' in kwargs:
            return models.Teacher.objects.get(id=kwargs['id'])
