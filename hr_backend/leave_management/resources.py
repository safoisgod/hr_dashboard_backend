from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User
from .models import Leave, LeaveType

class LeaveResource(resources.ModelResource):
    Employee = fields.Field(
        column_name= "employee",
        attribute= "employee",
        widget= ForeignKeyWidget(User,"username")
    )

    class Meta:
        model = Leave

class LeaveTypeResource(resources.ModelResource):
    class Meta:
        model = LeaveType 
