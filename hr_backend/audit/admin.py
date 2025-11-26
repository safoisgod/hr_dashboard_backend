from django.contrib import admin
from .models import AuditLog
from .resources import AuditLogResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(AuditLog)
class AuditLogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AuditLogResource
    
    list_display = ('user', 'action', 'timestamp', 'ip_address')
    search_fields = ('user__username', 'action', 'ip_address')
    list_filter = ('action', 'timestamp')

    def user(self, obj):
        return obj.user.username
    user.admin_order_field = 'user__username'