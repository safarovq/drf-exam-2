from django.db import models

# Create your models here.
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описания курса')
    duration = models.PositiveIntegerField(verbose_name='Продолжительность курса')

    def __str__(self):
        return self.name


class Grade(models.Model):
    value = models.PositiveIntegerField(verbose_name='Значения')
    date = models.DateField(verbose_name='Дата')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} - {self.course} ({self.value})'


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
