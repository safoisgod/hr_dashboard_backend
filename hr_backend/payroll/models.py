from django.db import models
from employees.models import Employee

# Create your models here.
class SalaryStructure(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    housing_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transport_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ssnit_deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    other_deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Salary Structure for {self.employee}"


class PayrollRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_structure = models.ForeignKey(SalaryStructure, on_delete=models.CASCADE)
    pay_date = models.DateField()
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    total_deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)