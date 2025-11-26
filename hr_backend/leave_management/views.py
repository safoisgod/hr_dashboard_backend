from django.shortcuts import render
from .models import Leave, LeaveType
from .serializers import LeaveSerializer, LeaveTypeSerializer, LeaveCreateSerializer, LeaveTypeCreateSerializer
from rest_framework import generics


# Create your views here.
class LeaveListCreateView(generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LeaveCreateSerializer
        return LeaveSerializer

class LeaveTypeListCreateView(generics.ListCreateAPIView):
    queryset = LeaveType.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LeaveTypeCreateSerializer
        return LeaveTypeSerializer

class LeaveDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class LeaveTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer

