from django.contrib import admin
from django.urls import path
from .views import LeaveListCreateView, LeaveTypeListCreateView, LeaveDetailView, LeaveTypeDetailView

urlpatterns = [
    path('leaves/', LeaveListCreateView.as_view(), name='leave-list-create'),
    path('leavetypes/', LeaveTypeListCreateView.as_view(), name='leavetype-list-create'),
    path('leaves/<int:pk>/', LeaveDetailView.as_view(), name='leave-detail'),
    path('leavetypes/<int:pk>/', LeaveTypeDetailView.as_view(), name='leavetype-detail'),
]