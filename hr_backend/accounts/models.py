from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    role_choices = [
        ('employee', 'Employee'),
        ('manager', 'Manager'),
        ('hr', 'HR'),
        ('admin', 'Admin'),
    ]

    username = models.CharField(max_length=150, unique=True)
    
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

    role = models.CharField(max_length=20, choices=role_choices, default='employee')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    is_employee = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"