from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    registration_no = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=16, unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='devices', null=True, blank=True)
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=255, unique=True)
    condition = models.CharField(max_length=255, default='Good')
    checked_out = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CheckoutLog(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='checkout_logs')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='checkout_logs')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='checkout_logs')
    checkout_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    condition_checkout = models.TextField(null=True, blank=True)
    condition_return = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.device} - {self.employee} - {self.checkout_date}"
