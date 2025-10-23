from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    snmp_port = models.IntegerField(default=161)
    community_string = models.CharField(max_length=100, default='public') # Mikrotik default
    is_active = models.BooleanField(default=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.ip_address})'
    
class DeviceStatus(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    status = models.CharField(max_length=10) #online or offline
    uptime = models.CharField(max_length=50, blank=True, null=True)
    polled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.device} - {self.status} at {self.polled_at}'
    
class JobRecord(models.Model):
    job_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20)
    result = models.TextField(null=True, blank=True)
    enqueued_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.job_id} - {self.status}"

class SNMPResult(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    oid = models.CharField(max_length=200)
    value = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.device} | {self.oid} | {self.value}'