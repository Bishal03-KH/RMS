from django.contrib import admin
from .models import House, Tenant, Room, TenantDocument, RentLedger, Payment, SMSLog, Expense, ReportExport

# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name','address','total_rooms')
    search_fields = ('name','address')
    
    
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
     list_display = ('full_name', 'phone', 'email', 'joined_date', 'is_active')
     search_fields = ('full_name', 'phone', 'email')
     
        

admin.site.register(Room)
admin.site.register(TenantDocument)
admin.site.register(RentLedger) 
admin.site.register(Payment)
admin.site.register(SMSLog)   
admin.site.register(Expense)
admin.site.register(ReportExport)