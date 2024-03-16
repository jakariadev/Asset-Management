from django.contrib import admin
from django.urls import path, include
from asset_app import views

urlpatterns = [
    path('company/', views.CompanyListView.as_view()),
    path('company/<int:pk>', views.CompanyDetailsView.as_view()),

    path('device/', views.DeviceListView.as_view()),
    path('device/<int:pk>', views.DeviceDetailsView.as_view()),

    path('employee/', views.EmployeeListView.as_view()),
    path('employee/<int:pk>', views.EmployeeDetailsView.as_view()),

    path('checkout-log/', views.CheckoutLogListView.as_view()),
    path('checkout-log/<int:pk>', views.CheckoutLogDetailsView.as_view()),
]
