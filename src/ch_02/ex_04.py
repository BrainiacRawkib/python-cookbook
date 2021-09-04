# matching and searching for text patterns
text = 'yeah, but no, but yeah, but no, but yeah'

# exact match
print(text == 'yeah')

# match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))

# search for the location of the first occurrence
print(text.find('no'))

if __name__ == '__main__':
    print()
