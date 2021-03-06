from netmiko import ConnectHandler

cisco_cloud_router = {'device_type': 'cisco_ios',
'ip': '10.0.0.5',
'username': 'ignw',
'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)

print(connection)
print(type(connection))
interface_output = connection.send_command('show run int g1')
print(interface_output)

hostname = connection.find_prompt()
print(hostname[:-1])

interface_name = connection.send_command('show run int g2 | i ^interface')
print(interface_name)
