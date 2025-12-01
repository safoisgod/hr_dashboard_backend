from django.contrib import admin
from .models import Department, Position, Employee
from import_export.admin import ImportExportModelAdmin
from .resources import DepartmentResource, PositionResource, EmployeeResource

# Register your models here.
@admin.register(Position)
class PositionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PositionResource #for import and export functionality
    
    list_display = ('id', 'title', 'get__department', 'created_at')
    search_fields = ('title', 'department__name')
    list_filter = ('department',)

    def get__department(self, obj):
        return obj.department.name
    get__department.short_description = 'Department'

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EmployeeResource  #for import and export functionality

    list_display = ('id', 'get__first_name', 'get__last_name', 'get__title', 'date_hired', 'is_active')
    search_fields = ('user__first_name', 'user__last_name', 'position__title')
    list_filter = ('is_active', 'position__title')

    def get__first_name(self, obj):
        return obj.user.first_name
    get__first_name.short_description = 'First Name'

    def get__last_name(self, obj):
        return obj.user.last_name
    get__last_name.short_description = 'Last Name'

    def get__title(self, obj):
        return obj.position.title
    get__title.short_description = 'Position'


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):    
    resource_class = DepartmentResource  #for import and export functionality
    
    list_display = ('id', 'name', 'get__manager', 'created_at')
    search_fields = ('name', 'user__username')

    def get__manager(self, obj):
        return obj.manager.username if obj.manager else 'N/A'
    get__manager.short_description = 'Manager'