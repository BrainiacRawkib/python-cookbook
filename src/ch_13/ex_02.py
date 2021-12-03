# terminating a program with an Error message

if __name__ == '__main__':
    import sys
    sys.stderr.write('It failed!\n')
    raise SystemExit('It failed!')
