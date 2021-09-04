# normalizing unicode text to a standard representation
import unicodedata

# unicode problems
s1 = 'SPicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)

print(s1 == s2)
print(len(s1), len(s2))

# fixing unicode problem with unicodedata
t1 = unicodedata.normalize('NFC', s1)  # *not working
t2 = unicodedata.normalize('NFC', s2)  # *not working
print(t1 == t2)  # *not working
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)  # *not working
t4 = unicodedata.normalize('NFD', s2)  # *not working
print(t3 == t4)  # *not working
print(ascii(t3))

# NFKC, NFKD
s = '\ufb01'
print(s)
print('NFD --->', unicodedata.normalize('NFD', s))
print('NFKD --->', unicodedata.normalize('NFKD', s))
print('NFKC --->', unicodedata.normalize('NFKC', s))

# removing all diacritical marks from some text
t1 = unicodedata.normalize('NFD', s1)
''.join(c for c in t1 if not unicodedata.combining(c))
print('Combining text -->', t1)  # not working

if __name__ == '__main__':
    pass
