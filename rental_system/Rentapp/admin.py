from django.contrib import admin
from .models import (
    House, Tenant, Room, TenantRecordManagement,
    MonthlyRent, Payment, SMSTemplate, SMSLog,
    Expense, Income
)

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'total_rooms', 'is_available')
    search_fields = ('name', 'address')

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'joined_date', 'is_active')
    search_fields = ('full_name', 'phone', 'email')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('house', 'room_number', 'tenant', 'monthly_rent', 'is_available')
   
@admin.register(TenantRecordManagement)
class TenantRecordManagementAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'room', 'contract_start', 'contract_end', 'monthly_rent', 'is_active')
    

@admin.register(MonthlyRent)
class MonthlyRentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'room', 'month', 'due_date', 'amount', 'is_paid')
    list_filter = ('is_paid', 'month')
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'rent', 'amount', 'payment_method', 'payment_date')
  
   
@admin.register(SMSTemplate)
class SMSTemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SMSLog)
class SMSLogAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'template', 'status', 'sent_at')
    

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('house', 'title', 'amount', 'date')
  

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('house', 'title', 'amount', 'date')
   