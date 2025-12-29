from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    House, Tenant, Room, TenantRecordManagement,
    MonthlyRent, Payment, SMSTemplate, SMSLog,
    Expense, Income
)
from .serializers import (
    HouseSerializer, TenantSerializer, RoomSerializer, 
    TenantRecordManagementSerializer, MonthlyRentSerializer,
    PaymentSerializer, SMSTemplateSerializer, SMSLogSerializer,
    ExpenseSerializer, IncomeSerializer
)

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    @action(detail=False, methods=['get'])
    def list_total_rooms(self, request):
        total_room_dict = {house.name: house.total_rooms for house in House.objects.all()}
        return Response(total_room_dict)

    @action(detail=False, methods=['get'])
    def house_available(self, request):
        available_count = House.objects.filter(is_available=True).count()
        unavailable_count = House.objects.filter(is_available=False).count()
        return Response({
            "available_count": available_count,
            "unavailable_count": unavailable_count
        })

    @action(detail=False, methods=['post'])
    def add_house(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "New house successfully added."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def total_rent(self, request, pk=None):
        house = self.get_object()
        total_rent = sum(room.monthly_rent for room in house.rooms.all())
        return Response({"house_name": house.name, "total_rent": total_rent})

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class TenantRecordManagementViewSet(viewsets.ModelViewSet):
    queryset = TenantRecordManagement.objects.all()
    serializer_class = TenantRecordManagementSerializer

class MonthlyRentViewSet(viewsets.ModelViewSet):
    queryset = MonthlyRent.objects.all()
    serializer_class = MonthlyRentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class SMSTemplateViewSet(viewsets.ModelViewSet):
    queryset = SMSTemplate.objects.all()
    serializer_class = SMSTemplateSerializer

class SMSLogViewSet(viewsets.ModelViewSet):
    queryset = SMSLog.objects.all()
    serializer_class = SMSLogSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
