from django.shortcuts import render
from .models import Employee, Department, Position
from .serializers import EmployeeSerializers, DepartmentSerializers, PositionSerializers, EmployeeCreateSerializers, DepartmentCreateSerializers, PositionCreateSerializers
from rest_framework import generics

# for all employees
class EmployeeListViewAPI(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeCreateSerializers
        return EmployeeSerializers

# for detailed employees
class EmployeeDetailViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class DepartmentListViewAPI(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DepartmentCreateSerializers
        return DepartmentSerializers

class DepartmentDetailViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class PositionListViewAPI(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PositionCreateSerializers
        return PositionSerializers

class PositionDetailViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers
    
# from rest_framework import viewsets


# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers

# class DepartmentViewSet(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializers

# class PositionViewSet(viewsets.ModelViewSet):
#     queryset = Position.objects.all()
#     serializer_class = PositionSerializers

# Create your views here.
