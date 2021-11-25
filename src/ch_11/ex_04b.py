# indexing network objects
import ipaddress

net = ipaddress.ip_network('123.45.67.64/27')
print(net.num_addresses)
print(net[0])
print(net[1])
print(net[-1])
print(net[-2])

# checking for network membership
print(format('Checking Membership', '*^30'))
a = ipaddress.ip_address('123.45.67.69')
print(a in net)
b = ipaddress.ip_address('123.45.67.123')
print(b in net)

# specifying an ip address as an interface
print(format('Specifying Interface', '*^30'))
inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)
print(inet.ip)

if __name__ == '__main__':
    pass
