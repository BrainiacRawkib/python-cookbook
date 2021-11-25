# Generating a range of IP addresses from a CIDR address
import ipaddress

net = ipaddress.ip_network('123.45.67.64/27')
print(net)
for a in net:
    print(a)

print(format('net6', '*^10s'))
net6 = ipaddress.ip_network('2:3456:78:90ab:cd:ef01:23:30/125')
print(net6)
for a in net6:
    print(a)

if __name__ == '__main__':
    pass
