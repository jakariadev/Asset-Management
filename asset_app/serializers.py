from rest_framework import serializers
from .models import Company, Employee, Device, CheckoutLog


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class CheckoutLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckoutLog
        fields = ['id', 'company', 'device', 'employee', 'checkout_date', 'return_date', 'condition_checkout', 'condition_return']
