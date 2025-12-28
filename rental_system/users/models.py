from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
import uuid

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email,name,phone,password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name,phone=phone,username=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,phone,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_email_verified',True)
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email,name,phone,password, **extra_fields)
    
class User(AbstractUser):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=100, blank=True, null=True)   
    
    objects = UserManager()
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['name','phone']
    
    def __str__(self):
        return self.email
    
    def generate_email_verification_token(self):
        token = str(uuid.uuid4())
        self.email_verification_token = token
        self.save()
        
        return token

        

        
    