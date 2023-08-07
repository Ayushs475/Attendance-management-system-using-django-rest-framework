from django.urls import path
from .views import DepartmentAPI, StudentAPI,CourseAPI,Attendance_logAPI # Import the necessary view classes

urlpatterns = [
    path('departments/', DepartmentAPI.as_view(), name='department'),
    path('students/', StudentAPI.as_view(), name='student'),
    path('Course/',CourseAPI.as_view(),name='course'),
    path('Course/',Attendance_logAPI.as_view(),name='course'),
    # Other URL patterns
]
