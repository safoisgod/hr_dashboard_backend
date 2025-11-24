from django.contrib import admin
from .models import Leave, LeaveType
# Register your models here.
@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('get__employee_name', 'get__leave_type', 'start_date', 'end_date', 'status', 'applied_on')
    search_fields = ('employee__user__first_name', 'employee__user__last_name', 'leave_type__name', 'status')
    list_filter = ('status', 'leave_type')

    def get__employee_name(self, obj):
        return f"{obj.employee.user.first_name} {obj.employee.user.last_name}"
    get__employee_name.short_description = 'Employee Name'

    def get__leave_type(self, obj):
        return obj.leave_type.name