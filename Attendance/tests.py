from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Department, Student, Course, Attendance_log
from .serializers import DepartmentSerializer, StudentSerializer, CourseSerializer, Attendance_logSerializer

class BaseAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

class DepartmentAPITestCase(BaseAPITestCase):
    def test_get_departments(self):
        response = self.client.get('/api/departments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_department(self):
        data = {'name': 'Test Department'}
        response = self.client.post('/api/departments/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Department.objects.count(), 1)
        self.assertEqual(Department.objects.get().name, 'Test Department')

    def test_update_department(self):
        department = Department.objects.create(name='Initial Department')
        updated_data = {'name': 'Updated Department'}
        response = self.client.put(f'/api/departments/{department.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        department.refresh_from_db()
        self.assertEqual(department.name, 'Updated Department')

    def test_partial_update_department(self):
        department = Department.objects.create(name='Initial Department')
        updated_data = {'name': 'Updated Department'}
        response = self.client.patch(f'/api/departments/{department.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        department.refresh_from_db()
        self.assertEqual(department.name, 'Updated Department')

class StudentAPITestCase(BaseAPITestCase):
    def test_get_students(self):
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        data = {'name': 'Test Student'}
        response = self.client.post('/api/students/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().name, 'Test Student')


    def test_update_student(self):
        student = Department.objects.create(name='Initial Student')
        updated_data = {'name': 'Updated Student'}
        response = self.client.put(f'/api/student/{student.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        student.refresh_from_db()
        self.assertEqual(student.name, 'student Department')

    def test_partial_update_department(self):
        student = Student.objects.create(name='Initial student')
        updated_data = {'name': 'Updated Department'}
        response = self.client.patch(f'/api/departments/{student.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        student.refresh_from_db()
        self.assertEqual(student.name, 'Updated student')


class CourseAPITestCase(BaseAPITestCase):
    def test_get_courses(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        data = {'name': 'Test Course'}
        response = self.client.post('/api/courses/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().name, 'Test Course')

    def test_update_course(self):
        course = Course.objects.create(name='Initial Course')
        updated_data = {'name': 'Updated Course'}
        response = self.client.put(f'/api/courses/{course.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        course.refresh_from_db()
        self.assertEqual(course.name, 'Updated Course')

    def test_partial_update_course(self):
        course = Course.objects.create(name='Initial Course')
        updated_data = {'name': 'Updated Course'}
        response = self.client.patch(f'/api/courses/{course.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        course.refresh_from_db()
        self.assertEqual(course.name, 'Updated Course')

class AttendanceLogAPITestCase(BaseAPITestCase):
    def test_get_attendance_logs(self):
        response = self.client.get('/api/attendance-logs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_attendance_log(self):
        data = {'date': '2023-08-07', 'student': 1, 'status': 'present'}
        response = self.client.post('/api/attendance-logs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Attendance_log.objects.count(), 1)
        self.assertEqual(Attendance_log.objects.get().status, 'present')

    def test_update_attendance_log(self):
        attendance = Attendance_log.objects.create(name='Initial attendance')
        updated_data = {'name': 'Updated attendance'}
        response = self.client.put(f'/api/attendance/{attendance.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        attendance.refresh_from_db()
        self.assertEqual(attendance.name, 'Updated attendance')

    def test_partial_update_attendance_log(self):
        attendance = Attendance_log.objects.create(name='Initial attendance')
        updated_data = {'name': 'Updated attendance'}
        response = self.client.patch(f'/api/courses/{attendance.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        attendance.refresh_from_db()
        self.assertEqual(attendance.name, 'Updated attendance')

    
