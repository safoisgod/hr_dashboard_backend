from django.db import models
from accounts.models import User
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_departments')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions', null=True, blank=True)
    description = models.TextField(blank=True)
    level = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.department.name}"


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='employee_profile')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')
    date_hired = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.user:
            return f"{self.user.first_name} {self.user.last_name} - {self.position.title}"
        return f"Employee ID {self.id} - {self.position.title}"