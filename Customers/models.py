from django.db import models
import uuid
from Users.models import User

# Create your models here.
#customers(ModelForm) --- photos/poster ---- models --- billing


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=False)
    username = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    mobileNo = models.PositiveIntegerField(null=True, blank=False, unique=True, max_length = 10)
    companyName = models.CharField(max_length=200, null=True, blank=False)
    companyAddress = models.TextField(null=True, blank=False)
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