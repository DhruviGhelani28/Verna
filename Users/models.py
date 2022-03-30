
from datetime import timezone
from tkinter import CASCADE
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
#profile(ModelForm) ---- billing(like projects- each profile add many project) --- rolls----task--billingstatus

class Roll(models.Model):
    ROLL_TYPE=(
        ('Supplier','Supplier'),
        ('Worker','Worker'),
        ('Customer','Customer'),
        ('Agency','Agency'),
        ('Model','Model'),
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
 
class Registration(models.Model):
    roll = models.ForeignKey(Roll, on_delete=models.SET_NULL, null=True, blank=False)
 
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
    
