from django.db import models
from accounts.models import User

# Create your models here.
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view_audit_logs", "Can view audit logs"),
            ("can_add_audit_logs", "Can add audit logs"),
            ("can_manage_audit_logs", "Can manage audit logs"),
        ]   
    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"