from django.contrib import admin
from .models import Notification
from .resources import NotificationResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = NotificationResource

    list_display = ('id', 'get__user', 'message', 'is_read', 'created_on')
    search_fields = ('user__username', 'message')
    list_filter = ('is_read', 'created_on')
    ordering = ('-created_on',)


    def get__user(self, obj):
        return obj.user.username
    get__user.short_description = 'User'
