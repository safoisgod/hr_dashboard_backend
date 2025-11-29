from rest_framework import serializers
from .models import AuditLog

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'

class AuditLogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = ['action', 'user', 'timestamp', 'ip_address']