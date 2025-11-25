from django.shortcuts import render
from rest_framework import generics
from .models import SalaryStructure, PayrollRecord
from .serializers import SalaryStructureSerializer, SalaryStructureCreateSerializer, PayrollRecordCreateSerializer, PayrollRecordSerializer

# Create your views here.
class SalaryStructureListCreateView(generics.ListCreateAPIView):
    queryset = SalaryStructure.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SalaryStructureCreateSerializer
        return SalaryStructureSerializer

class PayrollRecordListCreateView(generics.ListCreateAPIView):
    queryset = PayrollRecord.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PayrollRecordCreateSerializer
        return PayrollRecordSerializer

class SalaryStructureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaryStructure.objects.all()
    serializer_class = SalaryStructureSerializer

class PayrollRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PayrollRecord.objects.all()
    serializer_class = PayrollRecordSerializer