from netmiko import ConnectHandler
import os


user = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

router = {
    "device_type": "cisco_ios",
    "ip": "192.168.117.10",
    "username": user,
    "password": password
}

net_connect = ConnectHandler(**router)
output = net_connect.send_command("show ip int brief")
print(output)