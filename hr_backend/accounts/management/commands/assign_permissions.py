from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **options):

        admin = Group.objects.get(name='Admin')
        hr_manager = Group.objects.get(name='HR Manager')
        manager = Group.objects.get(name='Manager')
        employee = Group.objects.get(name='Employee')

        # account permissions
        view_user_permission = Permission.objects.get(codename='can_view_user_data')
        admin.permissions.add(view_user_permission)
        hr_manager.permissions.add(view_user_permission)
        manager.permissions.add(view_user_permission)
        employee.permissions.add(view_user_permission)

        add_user_permission = Permission.objects.get(codename='can_edit_user_data')
        admin.permissions.add(add_user_permission)
        hr_manager.permissions.add(add_user_permission)
        manager.permissions.add(add_user_permission)
        # Employees do not get edit permission

        manage_roles_permission = Permission.objects.get(codename='can_manage_roles')
        admin.permissions.add(manage_roles_permission)



        # employee attendance permissions
        view_attendance_permission = Permission.objects.get(codename='can_view_attendance')
        admin.permissions.add(view_attendance_permission)
        hr_manager.permissions.add(view_attendance_permission)
        manager.permissions.add(view_attendance_permission)
        employee.permissions.add(view_attendance_permission)

        edit_attendance_permission = Permission.objects.get(codename='can_edit_attendance')
        admin.permissions.add(edit_attendance_permission)
        hr_manager.permissions.add(edit_attendance_permission)
        manager.permissions.add(edit_attendance_permission)
        # Employees do not get edit permission

        manage_attendance_permission = Permission.objects.get(codename='can_manage_attendance')
        admin.permissions.add(manage_attendance_permission)

        # audit log permissions
        view_audit_logs_permission = Permission.objects.get(codename='can_view_audit_logs')
        admin.permissions.add(view_audit_logs_permission)
        hr_manager.permissions.add(view_audit_logs_permission)
        manager.permissions.add(view_audit_logs_permission)
        # Employees do not get view audit logs permission

        add_audit_logs_permission = Permission.objects.get(codename='can_add_audit_logs')
        admin.permissions.add(add_audit_logs_permission)
        hr_manager.permissions.add(add_audit_logs_permission)
        manager.permissions.add(add_audit_logs_permission)
        # Employees do not get add audit logs permission

        manage_audit_logs_permission = Permission.objects.get(codename='can_manage_audit_logs')
        admin.permissions.add(manage_audit_logs_permission)
        # Only Admin gets manage audit logs permission

        # leave management permissions
        view_leave_permission = Permission.objects.get(codename='can_view_leave')
        admin.permissions.add(view_leave_permission)
        hr_manager.permissions.add(view_leave_permission)
        manager.permissions.add(view_leave_permission)
        employee.permissions.add(view_leave_permission)

        approve_leave_permission = Permission.objects.get(codename='can_approve_leave')
        admin.permissions.add(approve_leave_permission)
        hr_manager.permissions.add(approve_leave_permission)        
        manager.permissions.add(approve_leave_permission)
        # Employees do not get approve leave permission

        reject_leave_permission = Permission.objects.get(codename='can_reject_leave')
        admin.permissions.add(reject_leave_permission)
        hr_manager.permissions.add(reject_leave_permission)
        manager.permissions.add(reject_leave_permission)
        # Employees do not get reject leave permission

        cancel_leave_permission = Permission.objects.get(codename='can_cancel_leave')
        admin.permissions.add(cancel_leave_permission)
        hr_manager.permissions.add(cancel_leave_permission)
        manager.permissions.add(cancel_leave_permission)
        employee.permissions.add(cancel_leave_permission)

        manage_leave_types_permission = Permission.objects.get(codename='can_manage_leave_types')
        admin.permissions.add(manage_leave_types_permission)
        # Only Admin gets manage leave types permission

        # notifications permissions
        # view notification
        view_notifications_permission = Permission.objects.get(codename='can_view_notifications')
        admin.permissions.add(view_notifications_permission)
        hr_manager.permissions.add(view_notifications_permission)
        manager.permissions.add(view_notifications_permission)
        employee.permissions.add(view_notifications_permission)

        # manage notifications
        manage_notifications_permission = Permission.objects.get(codename='can_manage_notifications')
        admin.permissions.add(manage_notifications_permission)
        hr_manager.permissions.add(manage_notifications_permission)
        manager.permissions.add(manage_notifications_permission)

        # employees do not get manage notifications permission

        # salary structure permissions
        view_salary_structure_permission = Permission.objects.get(codename='can_view_salary_structure')
        admin.permissions.add(view_salary_structure_permission)
        hr_manager.permissions.add(view_salary_structure_permission)
        manager.permissions.add(view_salary_structure_permission)
        employee.permissions.add(view_salary_structure_permission)
        
        edit_salary_structure_permission = Permission.objects.get(codename='can_edit_salary_structure')
        admin.permissions.add(edit_salary_structure_permission)
        hr_manager.permissions.add(edit_salary_structure_permission)
        manager.permissions.add(edit_salary_structure_permission)
        # employees do not get edit salary structure permission

        manage_salary_structure_permission = Permission.objects.get(codename='can_manage_salary_structure')
        admin.permissions.add(manage_salary_structure_permission)
        hr_manager.permissions.add(manage_salary_structure_permission)
        # only admin and hr manager get manage salary structure permission

        # payroll record permissions
        view_payroll_record_permission = Permission.objects.get(codename='can_view_payroll_record')
        admin.permissions.add(view_payroll_record_permission)
        hr_manager.permissions.add(view_payroll_record_permission)
        manager.permissions.add(view_payroll_record_permission)
        employee.permissions.add(view_payroll_record_permission)

        edit_payroll_record_permission = Permission.objects.get(codename='can_edit_payroll_record')
        admin.permissions.add(edit_payroll_record_permission)
        hr_manager.permissions.add(edit_payroll_record_permission)
        manager.permissions.add(edit_payroll_record_permission)
        # employees do not get edit payroll record permission

        manage_payroll_record_permission = Permission.objects.get(codename='can_manage_payroll_record')
        admin.permissions.add(manage_payroll_record_permission)
        hr_manager.permissions.add(manage_payroll_record_permission)
        # only admin and hr manager get manage payroll record permission