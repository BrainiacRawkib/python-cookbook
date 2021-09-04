# writing a regular expression for multiline patterns
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
               multiline comment */
        '''
regex_text = comment.findall(text1)
print('text1 -->', regex_text)

regex_text = comment.findall(text2)
print('text2 -->', regex_text)

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
regex_text = comment.findall(text2)
print('text2 -->', regex_text)

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
regex_text = comment.findall(text2)
print('text2 -->', regex_text)

if __name__ == '__main__':
    pass
