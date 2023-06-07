from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Student, Grade
from .serializers import CourseSerializer, StudentSerializer, GradeSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['POST'])
    def add_course(self, request, pk=None):
        student = self.get_object()
        course_id = request.data.get('course_id')
        course = Course.objects.get(pk=course_id)
        student.courses.add(course)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def set_grade(self, request, pk=None):
        student = self.get_object()
        course_id = request.data.get('course_id')
        grade_value = request.data.get('grade_value')
        course = Course.objects.get(pk=course_id)
        grade = Grade.objects.create(value=grade_value, course=course, student=student)
        grade_serializer = GradeSerializer(grade)
        return Response(grade_serializer.data, status=status.HTTP_201_CREATED)
