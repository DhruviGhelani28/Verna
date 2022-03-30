from re import T
from django.contrib import admin
from .models import Registration, Roll, BillStatus, Billing, OrderStatus, Task
# Register your models here.

admin.site.register(Roll)
admin.site.register(BillStatus)
admin.site.register(Billing)
admin.site.register(Registration)
admin.site.register(OrderStatus)
admin.site.register(Task)
