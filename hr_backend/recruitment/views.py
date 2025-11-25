from django.shortcuts import render
from .serializers import JobPostSerializer, ApplicationSerializer, JobPostCreateSerializer, ApplicationCreateSerializer
from rest_framework import generics
from .models import JobPost, Application
# Create your views here.

class JobPostListCreateView(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return JobPostCreateSerializer
        return JobPostSerializer
    
class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ApplicationCreateSerializer
        return ApplicationSerializer

class JobPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer