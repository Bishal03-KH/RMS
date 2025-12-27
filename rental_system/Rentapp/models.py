from django.db import models

# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    total_rooms = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name

class Tenant(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,unique=True)
    email = models.EmailField(blank =True,null=True)
    joined_date = models.DateField()
    is_active = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.full_name
    
class Room(models.Model):
    house = models.ForeignKey(House,on_delete=models.CASCADE,related_name="rooms") 
    room_number = models.CharField(max_length=30)  
    tenant = models.ForeignKey(Tenant,on_delete=models.SET_NULL,null=True,blank=True)
    monthly_rent = models.DecimalField(max_digits=10,decimal_places=2)
    
    is_available = models.BooleanField(default=True) 
    
    def __str__(self):
        return f"{self.house.name} - {self.room_number}"
    


class TenantDocument(models.Model):
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE) 
    document_name = models.CharField(max_length=100)
    file = models.FileField(upload_to="tenant_document/")  
    
    def __str__(self):
        return f"{self.tenant}-{self.document_name}"

class RentLedger(models.Model):
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE) 
    month = models.DateField()
    expected_amount = models.DecimalField(max_digits=10,decimal_places=4)
    due_date = models.DateField() 
    is_paid = models.BooleanField(default=False)   
    
    def __str__(self):
        return self.tenant.full_name
    
    
class Payment(models.Model):
    CHOICES =[
        ('online','Online'),
        ('cash','Cash')
    ]
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE,related_name='payments')  
    ledger = models.ForeignKey(RentLedger,on_delete=models.CASCADE) 
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_method = models.CharField(max_length=20,choices=CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.tenant.full_name
    
    
class SMSLog(models.Model):
    STATUS_CHOICES =[
        ('Delivered','delivered'),
        ('Failed','failed')
    ]
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default="Delivered")    
    
class Expense(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=4)
    date = models.DateField()     
    
class ReportExport(models.Model):
    report_type = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    file = models.FileField(upload_to="reports/")   
    created_at = models.DateTimeField(auto_now_add=True) 