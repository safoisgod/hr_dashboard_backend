from django.contrib import admin
from django.urls import path
from .views import SalaryStructureListCreateView, PayrollRecordListCreateView, SalaryStructureDetailView, PayrollRecordDetailView

urlpatterns = [
    path('salary-structures/', SalaryStructureListCreateView.as_view(), name='salary-structure-list-create'),
    path('salary-structures/<int:pk>/', SalaryStructureDetailView.as_view(), name='salary-structure-detail'),
    path('payroll-records/', PayrollRecordListCreateView.as_view(), name='payroll-record-list-create'),
    path('payroll-records/<int:pk>/', PayrollRecordDetailView.as_view(), name='payroll-record-detail'),
]