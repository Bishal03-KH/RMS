from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields =['email','name','password','confirm_password','phone']
        
    def validate(self,attrs):
        if attrs['password'] !=attrs['confirm_password']:
            raise serializers.ValidationError("Password doesnot match") 
        return attrs
    
    def create(self,validated_data):
        validated_data.pop('confirm_password') 
        user = User.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            phone = validated_data['phone'],
            password = validated_data['password']
        )
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self,attrs):
        email = attrs['email']
        password = attrs['password']
        user = authenticate(email=attrs['email'],password=attrs['password'])
        
        if email and password:
            user = authenticate(request=self.context.get('request'),email = email, password = password)
            
            if not user:
                raise serializers.ValidationError("Invalid email or passowrd.")
            attrs['user'] = user

            return attrs
        else:
            raise serializers.ValidationError("must include 'email' and 'password'.")
        

        

    