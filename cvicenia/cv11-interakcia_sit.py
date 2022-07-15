#!/usr/bin/env python3

from paramiko import SSHClient, AutoAddPolicy, client

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy)
client.connect("158.193.152.72", port=22, username="admin", password="class", look_for_keys=False, allow_agent=False, timeout=60)

#PARAMIKO cisco
stdin, stdout, stderr = client.exec_command("sh ip int br")
for riadok in stdout:
    zoznam = riadok.strip("\n").strip("\r").split(" ")
    for prvok in zoznam:
        if prvok == "":
            zoznam.remove(prvok)
    print(zoznam)

stdin, stdout, stderr = client.exec_command("sh version")
for riadok in stdout:
    print(riadok.strip("\n"))


client.close()