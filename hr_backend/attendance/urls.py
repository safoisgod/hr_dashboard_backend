from django.contrib import admin
from django.urls import path
from .views import AttendanceListViewAPI, AttendanceDetailViewAPI

urlpatterns = [
    path('attendances/', AttendanceListViewAPI.as_view(), name="attendance-list"),
    path('attendances/<int:pk>/', AttendanceDetailViewAPI.as_view(), name="attendance-detail"),
]