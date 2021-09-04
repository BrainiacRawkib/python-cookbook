import re
from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
        # return webbrowser.open(name)
    else:
        with open(name) as f:
            return f.read()


url = 'http://www.python.org'
match_url = re.match('http:|https:|ftp:', url)

if __name__ == '__main__':
    choices = ['http:', 'ftp:']
    # url.startswith(choices)  # TypeError: startswith first arg must be str or a tuple of str, not list
    url.startswith(tuple(choices))
    print(url)
    print(read_data(url))
    print(match_url)
