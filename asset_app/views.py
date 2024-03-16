from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceListView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class CheckoutLogListView(generics.ListCreateAPIView):
    queryset = CheckoutLog.objects.all()
    serializer_class = CheckoutLogSerializer


class CheckoutLogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CheckoutLog.objects.all()
    serializer_class = CheckoutLogSerializer




