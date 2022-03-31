
from datetime import timezone
import email
from tkinter import CASCADE
import uuid
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 
# Create your models here.
#profile(ModelForm) ---- billing(like projects- each profile add many project) --- rolls----task--billingstatus

class Roll(models.Model):
    ROLL_TYPE=(
        ('Supplier','Supplier'),
        ('Worker','Worker'),
        ('Customer','Customer'),
        ('Agency','Agency'),
        ('Model','Model'),
        ('Admin', 'Admin'),
    )
    name = models.CharField( max_length=100 , blank=False, null=True, choices=ROLL_TYPE )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True )
    
    def __str__(self) -> str:
        return str(self.name)
   
class BillStatus(models.Model):
    BILLSTATUS_TYPE=(
        ('Pending','Pending'),
        ('Clear','Clear'),
    )
    name = models.CharField( max_length=50 ,null=True, blank=False, choices=BILLSTATUS_TYPE )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True )
    
    def __str__(self) -> str:
        return str(self.name)   
  
class OrderStatus(models.Model):
    ORDERSTATUS_TYPE=(
        ('Not Given','Not Given'),
        ('Pending','Pending'),
        ('Clear','Clear'),
    )
    name = models.CharField( max_length=50 ,null=True, blank=False, choices=ORDERSTATUS_TYPE )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True )
    
    def __str__(self) -> str:
        return str(self.name)   
 
 
class Billing(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    username = models.CharField(max_length=50, null=True, blank=False)
    # client = models.ForeignKey(, on_delete=models.SET_NULL,null=True, blank=False)
    roll = models.ForeignKey(Roll, on_delete=models.SET_NULL, null=True, blank=False)
    status = models.ForeignKey(BillStatus, on_delete=models.SET_NULL, null=True, blank=False)
    orderstatus = models.ForeignKey(OrderStatus ,on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True, default= 0)
    date = models.DateTimeField(default=timezone.now,null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    
    def __str__(self) -> str:
        return str(self.client.name)

    
class Registration(models.Model):
    roll = models.ForeignKey(Roll, on_delete=models.SET_NULL, null=True, blank=False)

class CustomeAccountManager(BaseUserManager):
    """ Custome user manager class for new user and superuser """

    def create_superuser(self, email, username, first_name, last_name,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, last_name, password, **other_fields)

    def create_user(self, email, username, first_name, last_name, password , **other_fields):
        if not email:
            raise ValueError('You must provide an Email Address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        # user.set_password(confPassword)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custome user model to add extra feild in django table"""

    objects = CustomeAccountManager()
    username = models.CharField(max_length=100, null=True, blank=False, unique=True)
    email = models.EmailField(nall=True, blank=False, unique=True)
    first_name = models.CharField(max_length=100, null=True,blank=False)
    # last_name = models.CharField(max_length=100, null=True,blank=True)

    roll = models.ForeignKey(Roll,on_delete=models.SET_NULL, null=True, blank=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField('created',auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email','first_name','roll']
    def __str__(self) -> str:
        return str(self.username)

class Task(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=False )
    roll = models.ForeignKey(Roll,on_delete=models.CASCADE, null=True, blank=False)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    
    def __str__(self) -> str:
        return str(self.owner)