from rest_framework import serializers
from .models import SalaryStructure, PayrollRecord

class SalaryStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryStructure
        fields = '__all__'

class PayrollRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollRecord
        fields = '__all__'

class SalaryStructureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryStructure
        fields = ['employee', 'base_salary', 'housing_allowance', 'transport_allowance', 'other_allowances', 'bonus', 'tax_deductions', 'ssnit_deductions', 'other_deductions']

class PayrollRecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollRecord
        fields = ['employee', 'salary_structure', 'pay_date', 'gross_salary', 'total_deductions', 'net_salary']