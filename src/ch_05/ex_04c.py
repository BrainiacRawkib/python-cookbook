import array

nums = array.array('i', [1, 2, 3, 4, 5])

with open('data.bin', 'wb') as f:
    f.write(nums)

with open('data.bin', 'rb') as f:
    print(f.readinto(nums))

if __name__ == '__main__':
    pass
