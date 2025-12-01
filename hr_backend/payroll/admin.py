from django.contrib import admin
from .models import SalaryStructure, PayrollRecord
from .resources import PayrollRecordResource, SalaryStructureResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(SalaryStructure)
class SalaryStructureAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SalaryStructureResource

    list_display = ('id', 'get__employee', 'base_salary', 'housing_allowance', 'transport_allowance', 'other_allowances', 'bonus',)
    search_fields = ('employee__first_name', 'employee__last_name',)
    
    def get__employee(self, obj):
        return obj.employee.username
    get__employee.short_description = 'Employee'

@admin.register(PayrollRecord)
class PayrollRecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PayrollRecordResource
    
    list_display = ('id', 'get__employee', 'pay_date', 'gross_salary', 'total_deductions', 'net_salary',)
    search_fields = ('employee__first_name', 'employee__last_name',)
    
    def get__employee(self, obj):
        return obj.employee.username
    get__employee.short_description = 'Employee'
    