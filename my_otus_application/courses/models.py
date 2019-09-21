from django.db import models


# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=300)
    second_name = models.CharField(max_length=300)
    occupation = models.CharField(max_length=300)
    short_cv = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Lesson(models.Model):
    start_date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    homework = models.CharField(max_length=1000)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description}"


class Course(models.Model):
    course_name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=3, max_digits=10)
    duration = models.IntegerField(blank=True, null=True)
    teachers = models.ManyToManyField(Teacher, blank=True)
    lessons = models.ManyToManyField(Lesson, blank=True)

    def __str__(self):
        return f"{self.course_name}"

# registering new user: https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
