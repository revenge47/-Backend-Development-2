from django.contrib import admin
from .models import Device, DeviceStatus, JobRecord

# Register your models here.

admin.site.register(Device)
admin.site.register(DeviceStatus)
admin.site.register(JobRecord)
