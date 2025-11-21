from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer, CreateUserSerializer, UpdateUserSerializer

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.IsAdminUser]

class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    

class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [permissions.IsAdminUser]


class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
