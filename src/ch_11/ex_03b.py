# creating UDP client
# client.py
from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
print(s.sendto(b'', ('localhost', 20000)))
print(s.recvfrom(8192))

if __name__ == '__main__':
    pass
