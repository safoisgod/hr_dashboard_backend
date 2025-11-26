from django.shortcuts import render
from .models import AuditLog
from .serializers import AuditLogSerializer, AuditLogCreateSerializer
from rest_framework import generics

# Create your views here.
class AuditLogListCreateView(generics.ListCreateAPIView):
    queryset = AuditLog.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AuditLogCreateSerializer
        return AuditLogSerializer

class AuditLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer