from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'middle_name', 'last_name',
            'email', 'phone', 'role', 'profile_picture', 'is_employee', 'is_hr'
        ]

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =[
            'username', 'first_name', 'middle_name', 'last_name',
            'email', 'phone', 'role', 'password'
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            first_name = validated_data.get('first_name', ''),
            middle_name = validated_data.get('middle_name', ''),
            last_name = validated_data.get['last_name', ''],
            email = validated_data['email'],
            phone = validated_data['phone'],
            role = validated_data.get('role', 'employee'),
            password= validated_data['password']
        )

        return user
    
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'middle_name', 'last_name',
            'email', 'phone', 'role', 'profile_picture'
        ]
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.role = validated_data.get('role', instance.role)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance