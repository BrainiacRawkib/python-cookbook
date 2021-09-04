# reformatting text to a fixed number of columns
import os
import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(format('textwrap 70', '*^20s'))
print(textwrap.fill(s, 70))
print('\n'*2)
print(format('textwrap 40', '*^20s'))
print(textwrap.fill(s, 40))
print('\n'*2)
print(format('textwrap 40 initial_indent', '*^50s'))
print(textwrap.fill(s, 40, initial_indent='    '))
print('\n'*2)
print(format('textwrap 40 subsequent_indent', '*^50s'))
print(textwrap.fill(s, 40, subsequent_indent='    '))

print(format('Get terminal size', '*^40'))
# print(os.get_terminal_size().columns)  #  works in the terminal

if __name__ == '__main__':
    pass
