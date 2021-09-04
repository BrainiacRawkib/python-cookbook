from fnmatch import fnmatchcase

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

match_addr_case = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
match_addr_case2 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]

if __name__ == '__main__':
    print(match_addr_case)
    print(match_addr_case2)
