from django.db import models
from accounts.models import User
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=50, unique=True)
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='employee_profile')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')
    date_hired = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"