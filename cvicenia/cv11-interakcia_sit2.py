#!/usr/bin/env python3

from netmiko import ConnectHandler
from netmiko.scp_functions import verifyspace_and_transferfile

cisco = {
    "device_type": "cisco_ios",
    "host": "158.193.152.72",
    "username": "admin",
    "password": "class",
    "port": 22
}

client = ConnectHandler(**cisco)

# vystup = client.send_command("sh version")
# print(vystup)
vystup = client.send_command("sh ip int br")
print(vystup)

loop = [
    "int lo10",
    "ip add 1.2.3.4 255.255.255.255",
    "no sh"
]
vystup = client.send_config_set(loop)
print(vystup)

vystup = client.send_command("sh ip int br")
print(vystup)
