from django.db import models
from employees.models import Department

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.posted_date}"

class Application(models.Model):
    status_choices = [
        ('PENDING', 'Pending'),
        ('REVIEWED', 'Reviewed'),
        ('INTERVIEW', 'Interview Scheduled'),
        ('REJECTED', 'Rejected'),
        ('HIRED', 'Hired'),
    ]
    
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)
    applied_date = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(max_length=20, choices=status_choices, default='PENDING')

    def __str__(self):
        return f"{self.applicant_name} - {self.job_post.title}"