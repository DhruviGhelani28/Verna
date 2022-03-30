from doctest import BLANKLINE_MARKER
from email.policy import default
from operator import truediv
from platform import mac_ver
from pyexpat import model
from tkinter.tix import Balloon
from django.db import models
import uuid
from Users.models import OrderStatus,User
# Create your models here.
#suppliers(ModelForm) --- garments ---- billing


class Supplier(models.Model):
    supplier = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=False)
    username = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    mobileNo = models.IntegerField(null=True, blank=False, unique=True, max_length = 10)
    organisationName = models.CharField(max_length=200, null=True, blank=False)
    organisationAddress = models.TextField(null=True, blank=False)
    profile_image = models.ImageField(null = True, blank = True, upload_to = "profiles/", default = "profiles/user-default.png")
    location = models.CharField(max_length=200, blank = True, null = True)
    social_github = models.CharField(max_length=200, null=True, blank = True)
    social_twitter = models.CharField(max_length=200, null=True, blank = True)
    social_linkedin = models.CharField(max_length=200, null=True, blank = True)
    social_youtube = models.CharField(max_length=200, null=True, blank = True)
    social_website = models.CharField(max_length=200, null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, editable=False, primary_key=True, unique= True)
    
    def __str__(self) -> str:
        return str(self.name)
    
class Garment(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, null=True, blank=False)
    GarmentName = models.CharField(max_length=100, null=True, blank=False)
    price = models.IntegerField(null=True, blank=False)
    TimeDurationFrom = models.DateField(null=True, blank=False)
    TimeDurationTo = models.DateField(null=True, blank=False)
    orderstatus = models.ForeignKey(OrderStatus,on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    
    def __str__(self) -> str:
        return str(self.GarmentName)
    

    
    