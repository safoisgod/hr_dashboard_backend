from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import AuditLog
from django.contrib.auth.models import User

class AuditLogResource(resources.ModelResource):
    user = fields.Field(
        column_name= 'user',
        attribute= 'user',
        widget= ForeignKeyWidget(User, 'username')
    )

    class Meta:
        model = AuditLog