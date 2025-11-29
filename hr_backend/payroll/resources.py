from import_export import resources, fields
from . models import SalaryStructure, PayrollRecord
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User


class SalaryStructureResource(resources.ModelResource):
    employee = fields.Field(
        column_name='employee',
        attribute='employee',
        widget= ForeignKeyWidget(User, 'username')
    )

    class Meta:
        model = SalaryStructure


class PayrollRecordResource(resources.ModelResource):
    employee = fields.Field(
        column_name='employee',
        attribute='employee',
        widget= ForeignKeyWidget(User, 'username')
    )
    
    class Meta:
        model = PayrollRecord