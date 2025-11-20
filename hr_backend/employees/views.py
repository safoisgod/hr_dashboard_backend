from django.shortcuts import render
from .models import Employee, Department, Position
from .serializers import EmployeeSerializers, DepartmentSerializers, PositionSerializers
from rest_framework import generics

# for all employees
class EmployeeListViewAPI(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

# for detailed employees
class EmployeeDetailViewAPI(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class DepartmentListViewAPI(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

class DepartmentDetailViewAPI(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class PositionListViewAPI(generics.ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers

class PositionDetailViewAPI(generics.RetrieveAPIView):
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
