# client.py
from socket import socket, AF_INET, SOCK_STREAM
from ch_11.ex_09 import client_authenticate

secret_key = b'peekaboo'

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 18000))
client_authenticate(s, secret_key)
s.send(b'Hello World')
resp = s.recv(1024)
