#
import ipaddress
from socket import socket, AF_INET, SOCK_STREAM

a = ipaddress.ip_address('127.0.0.1')
s = socket(AF_INET, SOCK_STREAM)
# s.connect((a, 8080))
s.connect((str(a), 8080))  # convert IPV4Address explicitly to str

if __name__ == '__main__':
    pass
