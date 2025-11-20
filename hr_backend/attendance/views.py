from django.shortcuts import render
from .models import Attendance
from .serializers import AttendanceSerializers
from rest_framework import generics

# Create your views here.
class AttendanceListViewAPI(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers

class AttendanceDetailViewAPI(generics.RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers