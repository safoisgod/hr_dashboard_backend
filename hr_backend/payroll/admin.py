from django.contrib import admin
from .models import SalaryStructure, PayrollRecord

# Register your models here.
@admin.register(SalaryStructure)
class SalaryStructureAdmin(admin.ModelAdmin):
    list_display = ('get__employee', 'base_salary', 'housing_allowance', 'transport_allowance', 'other_allowances', 'bonus',)
    search_fields = ('employee__first_name', 'employee__last_name',)
    
    def get__employee(self, obj):
        return obj.employee.username
    get__employee.short_description = 'Employee'

@admin.register(PayrollRecord)
class PayrollRecordAdmin(admin.ModelAdmin):
    list_display = ('get__employee', 'pay_date', 'gross_salary', 'total_deductions', 'net_salary',)
    search_fields = ('employee__first_name', 'employee__last_name',)
    
    def get__employee(self, obj):
        return obj.employee.username
    get__employee.short_description = 'Employee'
    