# loading modules from a remote machine using import hooks
# check ex_11_testcode

# navigate to ex_11_testcode
# open the terminal in ex_11_testcode and run
# python3 -m http.server 15000

if __name__ == '__main__':
    from urllib.request import urlopen
    print(format('fib.py', '*^10s'))
    u = urlopen('http://localhost:15000/fib.py')
    data = u.read().decode('utf-8')
    print(data)

    print(format('spam.py', '*^10s'))
    u = urlopen('http://localhost:15000/spam.py')
    data = u.read().decode('utf-8')
    print(data)
