from import_export import resources, fields
from .models import User

class UserResource(resources.ModelResource):
    class Meta:
        model = User

