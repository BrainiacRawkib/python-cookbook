import os

if not os.path.exists('missingfile.txt'):
    with open('missingfile.txt', 'xt') as f:  # 'wt' can be replaced for 'xt'
        text = 'i am a missing file.txt'
        f.write(text)
else:
    print('File already exists!')


if __name__ == '__main__':
    pass
