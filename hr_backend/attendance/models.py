from django.db import models
from employees.models import Employee

# Create your models here.
class Attendance(models.Model):
    attendance_status = [
        ("present", "Present"),
        ("absent", "Absent"),
        ("on_leave", "On Leave"),
        ("late", "Late"),
        ("half_day", "Half Day"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=attendance_status)

    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"