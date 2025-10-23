import asyncio
from django_rq import job
from .snmp import poll_snmp
from .models import SNMPResult, Device

@job
def poll_device(device_id, oid):
    """Poll a device asynchronously and save result"""
    device = Device.objects.get(id=device_id)

    async def run():
        result = await poll_snmp(device.ip_address, device.snmp_port, device.community_string, oid)
    
        SNMPResult.objects.create( #save even when there is error
            device=device,
            oid=oid,
            value=result
        )

    asyncio.run(run())