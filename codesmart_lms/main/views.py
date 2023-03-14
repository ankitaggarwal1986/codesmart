from django.shortcuts import render
from .serializers import TeacherSerializer, CourseCategorySerializer, CourseSerializer, StudentSerializer
from .models import Teacher, Course, CourseCategory, Student
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# Create your views here.

class TeacherListAPIView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class TeacherDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class CourseListAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CourseDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CourseCategoryListAPIView(ListCreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [IsAuthenticated]

class CourseCategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [IsAuthenticated]

class StudentListAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]



