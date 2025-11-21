from django.shortcuts import render
from rest_framework import generics
from .models import SalaryStructure, PayrollRecord
from .serializers import SalaryStructureSerializer, PayrollRecordSerializer

# Create your views here.
class SalaryStructureListCreateView(generics.ListCreateAPIView):
    queryset = SalaryStructure.objects.all()
    serializer_class = SalaryStructureSerializer

class PayrollRecordListCreateView(generics.ListCreateAPIView):
    queryset = PayrollRecord.objects.all()
    serializer_class = PayrollRecordSerializer

class SalaryStructureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaryStructure.objects.all()
    serializer_class = SalaryStructureSerializer

class PayrollRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PayrollRecord.objects.all()
    serializer_class = PayrollRecordSerializer