from django.db import models
import uuid
from Users.models import OrderStatus, Roll,User

# Create your models here.
#agencies(ModelForm) --- premises --- billing--task


class Agency(models.Model):
    agency = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=100,null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    username = models.CharField(max_length=50, null=True, blank=False)
    roll = models.ForeignKey(Roll, on_delete=models.SET_NULL, null=True, blank=False)
    mobileNo = models.PositiveIntegerField(null=True, blank=False, unique=True, max_length = 10)
    agencyName = models.CharField(max_length=200, null=True, blank=False)
    agencyAddress = models.TextField(null=True, blank=False)
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
    
class Premise(models.Model):
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE, null=True, blank=False)
    ItemName = models.CharField(max_length=100, null=True, blank=False)
    price = models.IntegerField(null=True, blank=False)
    TimeDurationFrom = models.DateField(null=True, blank=False)
    TimeDurationTo = models.DateField(null=True, blank=False)
    orderstatus = models.ForeignKey(OrderStatus,on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    
    def __str__(self) -> str:
        return str(self.ItemName)
    