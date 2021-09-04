# sanitizing and cleaning up text
import unicodedata
import sys

# “pýtĥöñ”
s = 'pýtĥöñ\fis\tawesome\r\n'

print(s)

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}

# alternative to remap


def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', '')
    s = s.replace('\f', '')
    return s


a = s.translate(remap)
print(a)

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)

print(b.translate(cmb_chrs))

if __name__ == '__main__':
    pass
