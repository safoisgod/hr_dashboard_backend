from .models import AuditLog
from django.urls import path
from .views import AuditLogListCreateView, AuditLogDetailView

urlpatterns = [
    path('audit-logs',AuditLogListCreateView.as_view(), name='audit-log-list-create'),
    path('audit-logs/<int:pk>', AuditLogDetailView.as_view(), name='audit-log-detail'),
]   