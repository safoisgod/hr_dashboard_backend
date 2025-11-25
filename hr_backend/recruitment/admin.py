from django.contrib import admin
from .models import JobPost, Application

# Register your models here.
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'posted_date', 'is_active')
    list_filter = ('department', 'is_active', 'posted_date')
    search_fields = ('title', 'description', 'location')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'job_post', 'status', 'applied_date')
    list_filter = ('status', 'applied_date', 'job_post')
    search_fields = ('applicant_name', 'applicant_email', 'job_post__title')