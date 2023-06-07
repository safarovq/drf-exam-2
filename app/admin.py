from django.contrib import admin
from .models import Course, Student, Grade


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


class GradeAdmin(admin.ModelAdmin):
    pass
