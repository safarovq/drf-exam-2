from rest_framework import serializers
from .models import Course, Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'duration']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    grades = GradeSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
