# packing and unpacking large integers from bytes

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print(format('from bytes', '*^20s'))
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'), end='\n\n')

print(format('to bytes', '*^20s'))
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

if __name__ == '__main__':
    pass
