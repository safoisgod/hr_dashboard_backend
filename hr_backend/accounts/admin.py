from django.contrib import admin
from .models import User
from .resources import  UserResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UserResource

    list_display = ('username', 'first_name', 'last_name', 'email', 'role', 'is_employee', 'is_hr')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('role', 'is_employee', 'is_hr')