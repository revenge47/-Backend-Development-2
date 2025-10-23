import asyncio
from pysnmp.hlapi.asyncio import *
from pysnmp.smi.rfc1902 import ObjectIdentity, ObjectType

async def poll_snmp(ip, port, community, oid):
    print('[*]Starting service')
    with Slim(1) as slim:
        try:
            oids = [ObjectType(ObjectIdentity(oid))]
            errorIndication, errorStatus, errorIndex, varBinds = await slim.get(
            community,
            ip,
            port,
            *oids
        )
        except Exception as e:
            print(f"Exception during SNMP get: {e}")
        
    if errorIndication:
        return f'Error: {errorIndication}'
    elif errorStatus:
        return f"[!]SNMP error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex)-1][0] or '?'}"
    else:
        for varBind in varBinds:
            return' = '.join([x.prettyPrint() for x in varBind])
   


# if __name__ == '__main__':
#     asyncio.run(poll_snmp('127.0.0.1', 16100, 'public', '1.3.6.1.2.1.1.3.0'))














# def poll_snmp(ip, port, community, oid):
#     iterator = getCmd(
#         SnmpEngine(),
#         CommunityData(community, mpModel=0),
#         UdpTransportTarget((ip, port), timeout=2, retries=1),
#         ContextData(),
#         ObjectType(ObjectIdentity(oid))
#     )

#     errorIndication, errorStatus, errorIndex, varBinds = iterator #next(iterator)

#     if errorIndication:
#         return None, f"SNMP error: {errorIndication}"

#     elif errorStatus:
#         return None, f"SNMP error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex)-1][0] or '?'}"

#     else:
#         for varBind in varBinds:
#             return str(varBind[1]), None
