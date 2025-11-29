from import_export import resources, fields
from .models import JobPost, Application


class JobPostResource(resources.ModelResource):
    class Meta:
        model = JobPost

class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application