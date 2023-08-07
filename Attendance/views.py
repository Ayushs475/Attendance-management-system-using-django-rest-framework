import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework import status
from .models import *
from .serializers import *

logger = logging.getLogger(__name__)

class BaseAPI(APIView):
    """
    Base class for API views, providing common functionality.
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = None
    model_class = None

    def get(self, request):
        """
        Handle GET request to retrieve a list of objects.
        """
        logger.info(
            f'GET request received for {self.model_class.__name__}. '
            f'Method: {request.method}, URL: {request.get_full_path()}'
        )
        queryset = self.model_class.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        """
        Handle POST request to create a new object.
        """
        logger.info(
            f'POST request received for {self.model_class.__name__}. '
            f'Method: {request.method}, URL: {request.get_full_path()}'
        )
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status_code': 200, "payload": serializer.data, 'message': 'Data saved'})
        return Response({'status_code': 403, 'errors': serializer.errors, 'message': 'Invalid data'})

    def put(self, request, id):
        """
        Handle PUT request to update an existing object.
        """
        logger.info(
            f'PUT request received for {self.model_class.__name__}. '
            f'Method: {request.method}, URL: {request.get_full_path()}'
        )
        try:
            instance = self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            return Response({'status_code': 404, 'message': 'Object not found'})

        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status_code': 200, 'payload': serializer.data, 'message': 'Data updated'})
        return Response({'status_code': 403, 'errors': serializer.errors, 'message': 'Invalid data'})

    def patch(self, request, id):
        """
        Handle PATCH request to partially update an existing object.
        """
        logger.info(
            f'PATCH request received for {self.model_class.__name__}. '
            f'Method: {request.method}, URL: {request.get_full_path()}'
        )
        try:
            instance = self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            return Response({'status_code': 404, 'message': 'Object not found'})

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status_code': 200, 'payload': serializer.data, 'message': 'Data updated'})
        return Response({'status_code': 403, 'errors': serializer.errors, 'message': 'Invalid data'})

class DepartmentAPI(BaseAPI):
    """
    API view for Department model.
    """
    serializer_class = DepartmentSerializer
    model_class = Department

class StudentAPI(BaseAPI):
    """
    API view for Student model.
    """
    serializer_class = StudentSerializer
    model_class = Student

class CourseAPI(BaseAPI):
    """
    API view for Course model.
    """
    serializer_class = CourseSerializer
    model_class = Course

class Attendance_logAPI(BaseAPI):
    """
    API view for AttendanceLog model.
    """
    serializer_class = Attendance_logSerializer
    model_class = Attendance_log


def get_authentication_classes(self):
        """
        Returns the authentication classes for the view.
        """
        if self.request.resolver_match.url_name in self.unprotected_endpoints:
            return []
        return self.authentication_classes

class LoginAPI(BaseAPI):
    """
    API view for user login.
    """
    serializer_class = LoginSerializer
    model_class = User
    unprotected_endpoints = ['login']  # Exclude authentication for the login endpoint