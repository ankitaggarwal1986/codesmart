from django.urls import path
from . import views

urlpatterns = [
    path("", views.TeacherListAPIView.as_view(), name='teacher-list'),
    path("<int:pk>/", views.TeacherDetailAPIView.as_view(), name='teacher-detail'),
    path("course-list/", views.CourseListAPIView.as_view(), name='course-list'),
    path("course-list/<int:pk>/", views.CourseDetailAPIView.as_view(), name='course-detail'),
    path("course-category-list/", views.CourseCategoryListAPIView.as_view(), name='course-category-list'),
    path("course-category-list/<int:pk>/", views.CourseCategoryDetailAPIView.as_view(), name='teacher-detail'),
    path("student-list/", views.StudentListAPIView.as_view(), name='student-list'),
    path("student-list/<int:pk>/", views.StudentDetailAPIView.as_view(), name='student-detail'),
]
