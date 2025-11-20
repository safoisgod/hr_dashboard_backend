from django.contrib import admin
from django.urls import path
from .views import EmployeeListViewAPI, EmployeeDetailViewAPI, DepartmentListViewAPI, DepartmentDetailViewAPI, PositionListViewAPI, PositionDetailViewAPI

urlpatterns = [
    path('employees/', EmployeeListViewAPI.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailViewAPI.as_view(), name='employee-detail'),
    path('departments/', DepartmentListViewAPI.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailViewAPI.as_view(), name='department-detail'),
    path('positions/', PositionListViewAPI.as_view(), name='position-list'),
    path('positions/<int:pk>/', PositionDetailViewAPI.as_view(), name='position-detail'),
]
