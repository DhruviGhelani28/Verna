from distutils.command import upload
from email.policy import default
from pyexpat import model
from tokenize import blank_re
from unicodedata import name
import uuid
from django.db import models
from Users.models import User

# Create your models here.
# Workers(ModelForm) -----billing----task

class Worker(models.Model):
    worker = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(null=True, blank=False, max_length=50)
    username = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    mobileNo = models.BigIntegerField(null=True, blank=False)
    address = models.CharField(max_length=400, null=True, blank=False)
    short_intro = models.CharField(max_length=500, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True,upload_to="profiles/", default="profiles/user-default.png" )
    location = models.CharField(max_length=50, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    
    def __str__(self) -> str:
        return str(self.name)
    

