# searching and replacing case-insensitive text
import re

text = 'UPPER PYTHON, lower python, Mixed Python'

regex_text = re.findall('python', text, flags=re.IGNORECASE)
print(regex_text)

sub_text = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(sub_text)


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


matchcase_text = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(matchcase_text)

if __name__ == '__main__':
    print()
