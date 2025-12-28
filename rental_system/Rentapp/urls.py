from django.urls import path, include
from rest_framework import routers
from .views import (
    HouseViewSet, TenantViewSet, RoomViewSet, TenantDocumentViewSet,
    RentLedgerViewset, PaymentViewSet, SMSLogViewSet, ExpenseViewSet
)

router = routers.DefaultRouter()
router.register(r'houses', HouseViewSet, basename='house')
router.register(r'tenants', TenantViewSet, basename='tenant')
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'tenantdocuments', TenantDocumentViewSet, basename='tenantdocument')
router.register(r'rentledgers', RentLedgerViewset, basename='rentledger')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'smslogs', SMSLogViewSet, basename='smslog')
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls))
    
]
