from import_export import resources, fields
from .models import Attendance
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User


class AttendanceResources(resources.ModelResource):
    employee = fields.Field(
        column_name= 'employee',
        attribute= 'employee',
        widget= ForeignKeyWidget(User, 'username')
    )

    class Meta:
        model = Attendance
