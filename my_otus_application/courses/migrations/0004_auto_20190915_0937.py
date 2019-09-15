# Generated by Django 2.2.4 on 2019-09-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190915_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(blank=True, to='courses.Lesson'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, to='courses.Teacher'),
        ),
    ]
