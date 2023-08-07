from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.IntegerField(default=18)
    classroom = models.CharField(max_length=50)  # Changed 'class' to 'classroom'
    lecture_hours = models.IntegerField(default=18)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name

class Attendance_log(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    log_date = models.DateField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.log_date}"
    

class CustomUser(models.Model):
    # Define 'type' field with appropriate choices
    USER_TYPES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    type = models.CharField(max_length=10, choices=USER_TYPES)
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
