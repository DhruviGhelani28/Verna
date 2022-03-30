from django.contrib import admin
from .models import Garment, Supplier
# Register your models here.
admin.site.register(Supplier)
admin.site.register(Garment)