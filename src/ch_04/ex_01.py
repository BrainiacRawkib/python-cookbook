# manually consuming an iterator

# with open('/etc/passwd') as f:
#     try:
#         while True:
#             line = next(f)
#             print(line, end='')
#     except StopIteration:
#         pass

# if you're using next() and want to return the last value
# with open('/etc/passwd') as f:
#     while True:
#         line = next(f, None)
#         if line is None:
#             break
#         print(line, end='')


items = [1, 2, 3, 4]

# get the iterator
it = iter(items)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # StopIteration

if __name__ == '__main__':
    pass
