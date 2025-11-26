from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Department, Position, Employee
from django.contrib.auth.models import User

class DepartmentResource(resources.ModelResource):
    manager = fields.Field(
        column_name='manager',
        attribute='manager',
        widget=ForeignKeyWidget(User, 'first_name')
    )

    class Meta:
        model = Department

class PositionResource(resources.ModelResource):
    department = fields.Field(
        column_name='department',
        attribute='department',
        widget= ForeignKeyWidget(Department, 'name')
    )

    class Meta:
        model = Position

class EmployeeResource(resources.ModelResource):
    position = fields.Field(
        column_name= 'position',
        attribute='position',
         widget= ForeignKeyWidget(Position, 'title')
    )

    user = fields.Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(User, 'username')
    )

    class Meta:
        model = Employee