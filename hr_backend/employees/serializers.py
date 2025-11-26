from rest_framework import serializers
from accounts.models import User
from accounts.serializers import CreateUserSerializer
from .models import Department, Position, Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeCreateSerializers(serializers.ModelSerializer):
    user = CreateUserSerializer()
    class Meta:
        model = Employee
        fields = ['user', 'department', 'position', 'date_hired', 'is_active']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = CreateUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        employee = Employee.objects.create(user=user, **validated_data)
        return employee
class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'description', 'manager']
class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class PositionCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['title', 'description', 'department', 'level']
    