from django.db import models
from employees.models import Employee

# Create your models here.
class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Leave(models.Model):
    leave_status = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=leave_status, default="pending")
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_view_leave", "Can view leave"),
            ("can_approve_leave", "Can approve leave"),
            ("can_reject_leave", "Can reject leave"),
            ("can_cancel_leave", "Can cancel leave"),
            ("can_manage_leave_types", "Can manage leave types"),
        ]

    def __str__(self):
        return f"{self.employee.user.first_name} {self.employee.user.last_name} - {self.leave_type.name} ({self.start_date} to {self.end_date})"