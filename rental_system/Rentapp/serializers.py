from rest_framework import serializers
from .models import (
    House, Tenant, Room, TenantRecordManagement, 
    MonthlyRent, Payment, SMSTemplate, SMSLog,
    Expense, Income
)

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Tenant.objects.all(), source='tenant', write_only=True
    )

    class Meta:
        model = Room
        fields = ['id', 'house', 'room_number', 'monthly_rent', 'tenant', 'tenant_id', 'is_available']

class TenantRecordManagementSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Tenant.objects.all(), source='tenant', write_only=True
    )
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source='room', write_only=True
    )

    class Meta:
        model = TenantRecordManagement
        fields = ['id', 'tenant', 'tenant_id', 'room', 'room_id', 'contract_start', 'contract_end', 'monthly_rent', 'rental_agreement', 'id_proof', 'is_active']

class MonthlyRentSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Tenant.objects.all(), source='tenant', write_only=True
    )
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source='room', write_only=True
    )

    class Meta:
        model = MonthlyRent
        fields = ['id', 'tenant', 'tenant_id', 'room', 'room_id', 'month', 'due_date', 'amount', 'is_paid']

class PaymentSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Tenant.objects.all(), source='tenant', write_only=True
    )
    rent = MonthlyRentSerializer(read_only=True)
    rent_id = serializers.PrimaryKeyRelatedField(
        queryset=MonthlyRent.objects.all(), source='rent', write_only=True
    )

    class Meta:
        model = Payment
        fields = ['id', 'tenant', 'tenant_id', 'rent', 'rent_id', 'amount', 'payment_method', 'payment_date']

class SMSTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSTemplate
        fields = '__all__'

class SMSLogSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Tenant.objects.all(), source='tenant', write_only=True
    )
    template = SMSTemplateSerializer(read_only=True)
    template_id = serializers.PrimaryKeyRelatedField(
        queryset=SMSTemplate.objects.all(), source='template', write_only=True, allow_null=True, required=False
    )

    class Meta:
        model = SMSLog
        fields = ['id', 'tenant', 'tenant_id', 'template', 'template_id', 'message', 'sent_at', 'status']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"
