# Import libraries
from netmiko import ConnectHandler

cisco_cloud_router = {'device_type': 'cisco_ios',
'ip': '10.0.0.5',
'username': 'ignw',
'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)
#from device_info import ios_xe1 as device # noqa

# New Loopback Details
loopback = {"int_name": "Loopback103",
            "description": "Demo interface by CLI and netmiko",
            "ip": "192.168.103.1",
            "netmask": "255.255.255.0"}

# Create a CLI configuration
interface_config = [
    "interface {}".format(loopback["int_name"]),
    "description {}".format(loopback["description"]),
    "ip address {} {}".format(loopback["ip"], loopback["netmask"]),
    "no shut"
]

# Open CLI connection to device
with ConnectHandler(ip = "ip",
                    username = "username",
                    password = "password",
                    device_type = "device_type" as ch:

    # Send configuration to device
    output = ch.send_config_set(interface_config)

    # Print the raw command output to the screen
    print("The following configuration was sent: ")
print(output)
