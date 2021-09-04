# specifying a regular expression for the shortest match
import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
find_str = str_pat.findall(text1)
print(find_str)

text2 = 'Computer says "no." Phone says "yes."'
find_str2 = str_pat.findall(text2)
print('Problem --> ', find_str2)

str_pat = re.compile(r'\"(.*?)\"')  # add ? to fixed the greedy problem
text2 = 'Computer says "no." Phone says "yes."'
find_str2 = str_pat.findall(text2)
print('Problem Fixed --> ', find_str2)

if __name__ == '__main__':
    print()
