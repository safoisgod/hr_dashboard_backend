from django.contrib import admin
from .models import Attendance

# Register your models here.
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('username', 'date', 'check_in', 'check_out', 'status')
    search_fields = ('user__username', 'date', 'status')
    list_filter = ('status', 'date')

    def username(self, obj):
        return obj.employee.user.username
    username.admin_order_field = 'employee__user__username'