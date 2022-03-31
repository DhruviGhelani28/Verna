from logging import exception
from operator import contains
from typing_extensions import Required
from django.forms import ValidationError
from setuptools import Require
from . models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions

class UserRegistrationSerializer(serializers.ModelSerializer):
    """User registration serializer class"""
    username = serializers.CharField(required=True,help_text="Enter your Username.")
    email = serializers.CharField(required=True, help_text="Enter Your Email.")
    first_name = serializers.CharField(required=True,help_text="Enter your Name.")
    roll = serializers.CharField(required=True, help_text="Enter Your Roll.")
    password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'},help_text="Enter your Password.")
    confPassword = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'},help_text="Enter your Confirm Password.")

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs ={
            'is_active' :{
                'read_only':True
            },
            'is_superuser':{
                'read_only':True
            },
        }

    def validate_password(self, password, confPassword):
        if password == confPassword:
            if password.length >= 6:
                if password.contains('@') :
                    return password
                else:
                    raise serializers.ValidationError('There must be numbers & "@" in password')
            else:
                return serializers.ValidationError('Password must be of atleast 6 characters')
        else:
            raise serializers.ValidationError('Both Password Doesn\'t match')

    def validate_email(self, email):
        existing = User.object.filter(email=email).first()
        if existing:
            raise serializers.ValidationError('Someone with this username has already exist')
        else:
            if email.contains('@') and email.contains('.com'):
                return email
            else:
                raise serializers.ValidationError('Please enter correct email id')

    def validate_username(self, username):
        existing = User.objects.filter(username = username).first()
        if existing:
            raise serializers.ValidationError('Someone with this username has already exists')
        else:
            if username.contains('_'):
                return username
            else:
                raise serializers.ValidationError('Username must contain "_" ')

    def get_user_email(self,email):
        return email

    def create(self, validated_data):
        user = User.objects.create(
            username =validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            roll = validated_data['roll'],
            password = make_password(validated_data.get('password')),
            confPassword = make_password(validated_data.get('confPassword')),
        )
        return user


class AgencyProfileSerializer(serializers.ModelSerializer):
    agency = UserRegistrationSerializer(read_only =True)
    class Meta:
        model = Agency
        fields = ['id','agency','name','email','username','roll','mobileNo','agencyName','agencyAddress','profile_image','location','social_website']

    def create(self, validated_data):
        agencyProfile = Agency.objects.create(
            name = validated_data['name'],
            email = validated_data['email'],
            username = validated_data['username'],
            roll = validated_data['roll'],
            mobileNo = validated_data['mobileNo'],
            agencyName = validated_data['agencyName'],
            agencyAddress = validated_data['agencyAddress'],
            profile_image = validated_data['profile_image'],
            location = validated_data['location'],
            social_website = validated_data['social_website'],
        )
        return agencyProfile


class CustomerProfileSerializer(serializers.ModelSerializer):
    customer = UserRegistrationSerializer(read_only =True) 
    class Meta:
        model = Customer
        fields = ['id','user','name','email','username','roll','mobileNo','companyName','companyAddress','profile_image','location','social_website']

    def create(self, validated_data):
        customerProfile = Customer.objects.create(
            name = validated_data['name'],
            email = validated_data['email'],
            username = validated_data['username'],
            roll = validated_data['roll'],
            mobileNo = validated_data['mobileNo'],
            customerName = validated_data['customerName'],
            customerAddress = validated_data['customerAddress'],
            profile_image = validated_data['profile_image'],
            location = validated_data['location'],
            social_website = validated_data['social_website'],
        )
        return customerProfile


class SupplierProfileSerializer(serializers.ModelSerializer):
    supplier = UserRegistrationSerializer(read_only =True)
    class Meta:
        model = Supplier
        fields = '__all__'

    def create(self, validated_data):
        supplierProfile = Supplier.objects.create(
            name = validated_data['name'],
            email = validated_data['email'],
            username = validated_data['username'],
            roll = validated_data['roll'],
            mobileNo = validated_data['mobileNo'],
            organizationName = validated_data['organizationName'],
            organizationAddress = validated_data['organizationAddress'],
            profile_image = validated_data['profile_image'],
            location = validated_data['location'],
            social_website = validated_data['social_website'],
        )
        return supplierProfile


class WorkerProfileSerializer(serializers.ModelSerializer):
    worker = UserRegistrationSerializer(read_only =True)
    class Meta:
        model = Worker
        fields = '__all__'

    def create(self, validated_data):
        workerProfile = Agency.objects.create(
            name = validated_data['name'],
            email = validated_data['email'],
            username = validated_data['username'],
            roll = validated_data['roll'],
            mobileNo = validated_data['mobileNo'],
            address = validated_data['address'],
            short_intro = validated_data['short_intro'],
            profile_image = validated_data['profile_image'],
            location = validated_data['location'],   
        )
        return workerProfile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = '__all__'
        extra_kwargs = {
            'roll': {
            'read_only' : True
        },
        } 

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing 
        fields = '_all__'

class PremiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premise
        fields = '__all__'

class GarmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Garment
        fields = '__all__'

class UserApprovalSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=True)
    username = serializers.CharField(required=True, write_only = True,help_text="Enter your Username.")
    
    class Meta:
        model = User
        fields = ['id','is_activate','username','first_name','email']
        extra_kwargs ={
            'username':{
                'read_only':True
            },
            'first_name':{
                'read_only':True
            },
            'is_active':{
                'read_only':True
            },
            'email':{
                'read_only':True
            },
        }

    def update(self, instance, validated_data):
        if instance.username == validated_data['username']:
            instance.is_active = validated_data['is_active']
            instance.save()
        else:
            raise serializers.ValidationError('You are not right user')
        
        return instance

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_Password = serializers.CharField(write_only = True, required = True,style={'input_type': 'password'},help_text="Enter your old Password.") 
    new_Password = serializers.CharField(write_only = True, required = True,style={'input_type': 'password'},help_text="Enter your New Password.")
    conf_Password = serializers.CharField(write_only = True, required = True,style={'input_type': 'password'},help_text="Enter your Confirm Password.")

    class Meta:
        model = User
        fields = ['old_Password', 'new_Password','conf_Password']

    def validate(self,attrs):
        if attrs['new_password'] != attrs['conf_password']:
            raise serializers.ValidationError({"password":"Password fields doesn't match."})
        return attrs

    def validate_old_password(self,value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password":"Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        if validated_data['new_Password'] == validated_data['conf_Password']:
            instance.set_password(validated_data['new_Password'])
        else:
            raise serializers.ValidationError(' Password fields doesn\'t match')
        return super().update(instance, validated_data)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required = True, help_text = "Enter username")
    password = serializers.CharField(required = True, help_text = "Enter password", style={'input':'password'}) 
    roll = serializers.CharField(required=True)
    class Meta:
        model= User
        fields = '__all__'
    def validate(self, attrs):
        user = authenticate(**attrs)
        if user:
            if user.is_active:
                attrs['user'] = user
                return attrs
            raise exceptions.AuthenticationFailed('Account is not active')
        raise exceptions.AuthenticationFailed()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'