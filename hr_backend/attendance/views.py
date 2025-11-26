from django.shortcuts import render
from .models import Attendance
from .serializers import AttendanceSerializers, AttendanceCreateSerializer
from rest_framework import generics

# Create your views here.
class AttendanceListViewAPI(generics.ListAPIView):
    queryset = Attendance.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AttendanceCreateSerializer
        return AttendanceSerializers

class AttendanceDetailViewAPI(generics.RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers
