from rest_framework import serializers
from .models import Department, Position, Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'