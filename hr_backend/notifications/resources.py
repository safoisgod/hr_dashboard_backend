from .models import Notification
from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields
from django.contrib.auth.models import User
from .models import Notification

class NotificationResource(resources.ModelResource):
    user = fields.Field(
        column_name= "user",
        attribute= 'user',
        widget= ForeignKeyWidget(User, 'username')
    )

    class Meta:
        model = Notification