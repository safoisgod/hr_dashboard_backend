from django.shortcuts import render
from .models import AuditLog
from .serializers import AuditLogSerializer
from rest_framework import generics

# Create your views here.
class AuditLogListCreateView(generics.ListCreateAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer

class AuditLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer