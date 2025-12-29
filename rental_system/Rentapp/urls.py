from django.urls import path, include
from rest_framework import routers
from .views import (
    HouseViewSet, TenantViewSet, RoomViewSet,
    TenantRecordManagementViewSet, MonthlyRentViewSet,
    PaymentViewSet, SMSTemplateViewSet, SMSLogViewSet,
    ExpenseViewSet, IncomeViewSet
)

router = routers.DefaultRouter()
router.register(r'houses', HouseViewSet, basename='house')
router.register(r'tenants', TenantViewSet, basename='tenant')
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'tenant-records', TenantRecordManagementViewSet, basename='tenantrecord')
router.register(r'monthly-rents', MonthlyRentViewSet, basename='monthlyrent')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'sms-templates', SMSTemplateViewSet, basename='smstemplate')
router.register(r'sms-logs', SMSLogViewSet, basename='smslog')
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'incomes', IncomeViewSet, basename='income')

urlpatterns = [
    path('', include(router.urls))
]
