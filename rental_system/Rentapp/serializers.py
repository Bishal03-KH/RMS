from rest_framework import serializers

from .models import House, Tenant, Room, TenantDocument, RentLedger, Payment, SMSLog, Expense, ReportExport


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Tenant.objects.all(), source='tenant', write_only=True)

    class Meta:
        model = Room
        fields = ['id', 'house', 'room_number', 'monthly_rent',
                  'tenant', 'tenant_id', 'is_available']


class TenantDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantDocument
        fields = '__all__'


class RentLedgerSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Tenant.objects.all(), source='tenant', write_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source='room', write_only=True)

    class Meta:
        model = RentLedger
        fields = ['id', 'tenant', 'tenant_id', 'room', 'room_id',
                  'month', 'expected_amount', 'due_date', 'is_paid']


class PaymentSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    ledger = RentLedgerSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Tenant.objects.all(), source='tenant', write_only=True)
    ledger_id = serializers.PrimaryKeyRelatedField(
        queryset=RentLedger.objects.all(), source='ledger', write_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'tenant', 'tenant_id', 'ledger',
                  'ledger_id', 'amount', 'payment_method', 'payment_date']


class SMSLogSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    tenant_id = serializers.PrimaryKeyRelatedField(
        queryset=Tenant.objects.all(), source='tenant', write_only=True)
    class Meta:
        model = SMSLog
        fields = ['id','tenant','tenant_id','message','status','sent_at']
        
        
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"
        
class ReportExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportExport
        fields = '__all__'                
