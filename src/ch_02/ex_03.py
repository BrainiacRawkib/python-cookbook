# matching strings using shell wildcard patterns
from fnmatch import fnmatch, fnmatchcase

match_ext = fnmatch('foo.txt', '*.txt')
match_ext_case = fnmatchcase('foo.txt', '*.txt')
match_ext_case2 = fnmatchcase('foo.txt', '*.TXT')
match_ext2 = fnmatch('foo.txt', '?oo.txt')
match_ext3 = fnmatch('Dat45.csv', 'Dat[0-9]*')
match_ext3b = fnmatch('Dat45.csv', 'Dat[0-9]')

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py', 'Dat34.csv']
match_names = [name for name in names if fnmatch(name, 'Dat*.csv')]

if __name__ == '__main__':
    print(match_ext)
    print('match_ext_case -->', match_ext_case)
    print('match_ext_case2 -->', match_ext_case2)
    print(match_ext2)
    print(match_ext3)
    print(match_ext3b)
    print(match_names)
