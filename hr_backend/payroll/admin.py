from django.contrib import admin
from .models import SalaryStructure, PayrollRecord

# Register your models here.
admin.site.register(SalaryStructure)
admin.site.register(PayrollRecord)