from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, widgets
from .models import Registration
    
    

class SignUpForm(UserCreationForm):
    class Meta:
        model : Registration
        fields = UserCreationForm.Meta.fields + ('Roll')
        widgets