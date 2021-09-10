# reading and writing text data

# read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()

# read the entire file in a particular encoding format
with open('somefile.txt', 'rt', encoding='latin-1') as f:
    data2 = f.read()


# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
        # process line
        pass

# write chunks of text data
text = 'I am in writing mode'
with open('somefile.txt', 'wt') as f:
    f.write(text)

# append chunks of text data
text = 'I am in appending mode'
with open('somefile.txt', 'at') as f:
    f.write(text)
