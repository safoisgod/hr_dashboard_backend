from django.contrib import admin
from .models import JobPost, Application
from .resources import JobPostResource, ApplicationResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(JobPost)
class JobPostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = JobPostResource

    list_display = ('id', 'title', 'department', 'location', 'posted_date', 'is_active')
    list_filter = ('department', 'is_active', 'posted_date')
    search_fields = ('title', 'description', 'location')

@admin.register(Application)
class ApplicationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ApplicationResource
    
    list_display = ('id', 'applicant_name', 'job_post', 'status', 'applied_date')
    list_filter = ('status', 'applied_date', 'job_post')
    search_fields = ('applicant_name', 'applicant_email', 'job_post__title')