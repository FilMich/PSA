#!/usr/bin/env python3

from paramiko import SSHClient, AutoAddPolicy, client

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy)
client.connect("158.193.152.119", port=22, username="admin", password="class12345", look_for_keys=False, allow_agent=False, timeout=60)
 

stdin, stdout, stderr = client.exec_command("interface ether1 print terse")
for riadok in stdout:
    zoznam = riadok.strip("\n").strip("\r").split(" ")
    for prvok in zoznam:
        if prvok == "":
            zoznam.remove(prvok)
    print(zoznam[1] + " " + zoznam[2])

stdin, stdout, stderr = client.exec_command("int pr terse")
for riadok in stdout:
    zoznam = riadok.strip("\n").split(" ")
    if zoznam[2] == "name=ether1":
        print(zoznam[7])

client.close()