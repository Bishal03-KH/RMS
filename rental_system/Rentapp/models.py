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
    
    
class MonthlyRent(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='monthly_rents')
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='monthly_rents')
    month = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10,decimal_places=3)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.tenant.full_name

    
class Payment(models.Model):
    CHOICES =[
        ('online','Online'),
        ('cash','Cash')
    ]
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE,related_name='payments')  
    rent = models.ForeignKey(MonthlyRent,on_delete=models.CASCADE) 
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_method = models.CharField(max_length=20,choices=CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.tenant.full_name
    


class TenantRecordManagement(models.Model):
    tenant = models.OneToOneField(Tenant,on_delete=models.CASCADE,related_name="tenant_record")  
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True,blank=True)
    contract_start = models.DateField(null=True,blank=True)
    contract_end = models.DateField(null=True,blank=True)
    monthly_rent = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    rental_agreement = models.FileField(upload_to='documents/rentals/', blank=True, null=True)
    id_proof = models.FileField(upload_to='documents/id_proof/',blank=True,null=True)
    is_active = models.BooleanField(default=True) 
    
    def __str__(self):
        return f"{self.tenant.full_name} - {self.room}"
    

class SMSTemplate(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    
    
    
class SMSLog(models.Model):
    STATUS_CHOICES =[
        ('Delivered','delivered'),
        ('Failed','failed')
    ]
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE)
    template = models.ForeignKey(SMSTemplate, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default="Delivered")  
    
    def __str__(self):
        return f"{self.tenant.full_name} - {self.status}"  
    
    
    
class Expense(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE,related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=4)
    date = models.DateField()     
    
    def __str__(self):
        return f"{self.house.name} - {self.title} - {self.amount}"
    
    
class Income(models.Model):
    house = models.ForeignKey(House,on_delete=models.CASCADE,related_name='incomes')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=3)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.house.name} - {self.title} - {self.amount}"
        
