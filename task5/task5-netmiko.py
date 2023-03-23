
from netmiko import ConnectHandler 

device={
        "device_type": "cisco_ios", 
        "host":"192.168.56.101", 
        "port":"22", 
        "username":"cisco", 
        "password":"cisco123!" 
} 


commands = ["interface loopback 7", "ip address 14.15.16.17 255.255.255.0", "description test loopback netmiko","do show ip interface brief"] 

with ConnectHandler(**device) as net_connect: 
        output = net_connect.send_config_set(commands) 
        output += net_connect.save_config() 

print() 

print(output) 

print() 