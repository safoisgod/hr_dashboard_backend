from django.db import models
from accounts.models import User
# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions =[
            ('can_view_notifications', 'Can view notifications'),
            ('can_manage_notifications', 'Can manage notifications'),
        ]    
    def __str__(self):
        return f"Notification for {self.user.username} - {'Read' if self.is_read else 'Unread'}"